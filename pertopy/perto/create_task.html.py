{% extends 'base.html' %}

{% block content %}
  <h2>Create Task</h2>
  <form method="post">
    {% csrf_token %}
    {{ form.as_p }}
    <button type="submit" class="btn btn-primary">Create</button>
  </form>
{% endblock %}
