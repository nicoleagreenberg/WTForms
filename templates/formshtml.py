{% block content %}
  <h1>Simple WTF-Form</h1>
  <form method="POST" action="http://localhost:5000/result">
      {{ form.hidden_tag() }}
      {% for message in get_flashed_messages() %}
      {{ message }}
      {% endfor %}
      <p>{{ form.artist.label }}{{ form.name() }}</p>
      <p>{{ form.email.label }}{{ form.age() }}</p>
      <p>{{ form.email.label }}{{ form.age() }}</p>
      {{ form.submit() }}
  </form>
{% endblock %}