---
layout: archive
title: "Publications"
permalink: /publications/
author_profile: true
---

{% include base_path %}

<ul>
  {% for pub in site.data.publications.publications %}
    {% if pub %}
      <li>
        <a href="{{ pub.url }}">{{ pub.title }}</a> - {{ pub.authors }} ({{ pub.year }})
        <button class="citation-tab" onclick="toggleCitation({{ forloop.index }})">Citation</button>
        <!-- Hidden citation content that will be shown/hidden on button click -->
        <div id="citation-{{ forloop.index }}" class="citation-content" style="display: none;">
          <pre>{{ pub.citation }}</pre> <!-- Citation text from pub.citation -->
        </div> 
      </li>
    {% else %}
      <p>No publications data available for this entry</p>
    {% endif %}
  {% endfor %}
<ul>

<script>
  function toggleCitation(index) {
    const citationContent = document.getElementById("citation-" + index);
    if (citationContent.style.display === "none") {
      citationContent.style.display = "block";  // Show citation
    } else {
      citationContent.style.display = "none";  // Hide citation
    }
  }
</script>