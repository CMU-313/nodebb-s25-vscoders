'use strict';

const translatorApi = module.exports;

const PRIMARY_API = 'http://translator:5000/';
const FALLBACK_API = 'http://localhost:5000/';

let resolvedApiBase = null;

async function checkApiAvailable(apiUrl) {
	try {
		const testResponse = await fetch(`${apiUrl}?content=test`);
		return testResponse.ok;
	} catch (e) {
		return false;
	}
}

async function resolveApiBase() {
	if (await checkApiAvailable(PRIMARY_API)) {
		return PRIMARY_API;
	}
	if (await checkApiAvailable(FALLBACK_API)) {
		return FALLBACK_API;
	}
	throw new Error('No translator API available');
}

async function getApiBase() {
	if (!resolvedApiBase) {
		try {
			resolvedApiBase = await resolveApiBase();
			console.log(`Resolved translator API base to: ${resolvedApiBase}`);
		} catch (err) {
			console.error('Failed to resolve any translator API:', err);
			resolvedApiBase = PRIMARY_API;
		}
	}
	return resolvedApiBase;
}

translatorApi.translate = async function (postData) {
	try {
		const apiBase = await getApiBase();
		const response = await fetch(`${apiBase}?content=${encodeURIComponent(postData.content)}`);
		if (!response.ok) {
			throw new Error(`HTTP error! status: ${response.status}`);
		}
		const data = await response.json();
		return [data.is_english, data.translated_content];
	} catch (error) {
		console.error('Translation failed:', error);
		return [true, postData.content];
	}
};
