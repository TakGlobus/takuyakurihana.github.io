---
layout: archive
title: "Publications"
permalink: /publications/
author_profile: true
---


<h2>My Publications</h2>

<ul>
  {% for pub in site.data.publications %}
    <li>
      <a href="{{ pub.url }}">{{ pub.title }}</a> - {{ pub.authors }} ({{ pub.year }})
    </li>
  {% endfor %}
</ul>