<div class="row dashboard px-lg-4">
	<div class="col-12">
		<!-- IMPORT admin/partials/dashboard/graph.tpl -->
		<!-- IMPORT admin/partials/dashboard/stats.tpl -->
		<div class="table-responsive">
			<table class="table topics-list text-sm">
				<tbody>
					{{{ if !topics.length}}}
					<tr>
						<td colspan=4" class="text-center"><em>[[admin/dashboard:details.no-topics]]</em></td>
					</tr>
					{{{ end }}}
					{{{ each topics }}}
					<tr>
						<td><a href="{config.relative_path}/topic/{../slug}">{../title}</a></td>
						<td>[[topic:posted-by, {../user.username}]]</td>
						<td><span class="timeago" data-title="{../timestampISO}"></span></td>
					</tr>
					{{{ end }}}
				</tbody>
			</table>
		</div>

		<!-- public/templates/topic.tpl -->
		<div class="post">
			<div class="post-header">
				<span class="username">
					{{{ if post.anonymous }}}Anonymous{{{ else }}}{post.user.username}{{{ end }}}
				</span>
			</div>
			<div class="post-content">
				{post.content}
			</div>
		</div>
	</div>
</div>