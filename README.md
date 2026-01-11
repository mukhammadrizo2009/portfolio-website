# portfolio-website

portfolio/
 ├─ backend/
 │   ├─ core/
 │   ├─ apps/
 │   │   ├─ profile/
 │   │   ├─ skills/
 │   │   ├─ projects/
 │   │   └─ contact/
 │   ├─ manage.py
 │   └─ requirements.txt
 │
 ├─ templates/
 │   └─ index.html
 ├─ static/
 │   └─ style.css


<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>{{ profile.full_name }}</title>
    <style>
        body {
            background:#0f0f0f;
            color:white;
            font-family:Arial;
            padding:40px;
        }
        .skill {
            background:#1e1e1e;
            padding:10px;
            margin-bottom:10px;
            border-radius:8px;
        }
        .bar {
            height:8px;
            background:red;
            margin-top:5px;
            border-radius:5px;
        }
    </style>
</head>
<body>

{% if profile %}
  <h1>Hi, I'm {{ profile.full_name }}</h1>
  <h3>{{ profile.title }}</h3>
  <p>{{ profile.bio }}</p>
{% endif %}

<hr>

<h2>My Skills</h2>

{% for skill in skills %}
  <div class="skill">
      <strong>{{ skill.name }}</strong>
      <div class="bar" style="width: {{ skill.level }}%;"></div>
  </div>
{% empty %}
  <p>No skills added yet</p>
{% endfor %}

</body>
</html>
<hr>

<h2>My Projects</h2>

{% for project in projects %}
  <div style="background:#1e1e1e;padding:15px;margin-bottom:15px;border-radius:10px">
      <h3>{{ project.title }}</h3>
      <p>{{ project.description }}</p>
      <small>{{ project.tech_stack }}</small><br><br>

      {% if project.github_url %}
        <a href="{{ project.github_url }}" target="_blank">GitHub</a>
      {% endif %}

      {% if project.live_url %}
        | <a href="{{ project.live_url }}" target="_blank">Live</a>
      {% endif %}
  </div>
{% empty %}
  <p>No projects yet</p>
{% endfor %}

<hr>

<h2>Contact Me</h2>

<form method="post" action="/api/contact/">
  {% csrf_token %}
  <input type="text" name="name" placeholder="Your name" required><br><br>
  <input type="email" name="email" placeholder="Your email" required><br><br>
  <input type="telegram_username" name="telegram_username" placeholder="Your telegram username" required><br><br>
  <textarea name="message" placeholder="Your message" required></textarea><br><br>
  <button type="submit">Send</button>
</form>

