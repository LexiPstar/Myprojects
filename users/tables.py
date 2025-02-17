import django_tables2 as tables
from django.utils.html import format_html
from django.urls import reverse
from .models import User


class UserTable(tables.Table):
    id_select = tables.CheckBoxColumn(accessor="id", orderable=False, exclude_from_export=True)
    actions = tables.Column(empty_values=(), verbose_name="操作", orderable=False, exclude_from_export=True)

    class Meta:
        # 使用哪个模型
        model = User
        # 表格中显示哪些字段
        fields = ['username', 'email', 'first_name', 'last_name', 'is_staff']
        # 表格中字段显示顺序
        sequence = ['id_select'] + fields + ['actions']
        # 表格模板
        template_name = "users/bs4_tables2.html"
        # 表格样式
        attrs = {"class": "table table-striped table-sm text-nowrap"}
        # 排序字段
        order_by_field = 'sort_by'  # default: sort
        # page_field = 'page'

    # 自定义操作链接
    def render_actions(self, value, record):
        return format_html(
            '<a class="btn btn-sm badge badge-pill badge-warning ml-2" href= "' +
            reverse("users:user_update", args=[str(record.pk)]) + '">' + '编辑' + '</a>'
            + '<a class=" btn  btn-sm badge badge-pill badge-danger ml-2" href= "' +
            reverse("users:user_delete", args=[str(record.pk)]) + '">' + '删除' + '</a>'
        )
