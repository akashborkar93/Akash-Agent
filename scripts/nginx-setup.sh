#!/bin/bash
set -e

echo "Starting nginx webserver setup..."

# Update system packages
apt-get update -y
apt-get upgrade -y

# Install nginx
apt-get install -y nginx

# Start nginx service
systemctl start nginx
systemctl enable nginx

# Create a custom welcome page
cat > /var/www/html/index.html << 'EOF'
<!DOCTYPE html>
<html>
<head>
    <title>Akash-Agent Nginx Server</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 50px; }
        .container { max-width: 600px; }
        h1 { color: #333; }
        .info { background-color: #f0f0f0; padding: 15px; border-radius: 5px; }
    </style>
</head>
<body>
    <div class="container">
        <h1>🚀 Akash-Agent Webserver</h1>
        <div class="info">
            <p><strong>Status:</strong> ✅ Running</p>
            <p><strong>Server:</strong> Nginx</p>
            <p><strong>Environment:</strong> Production</p>
            <p><strong>Timestamp:</strong> <span id="timestamp"></span></p>
        </div>
    </div>
    <script>
        document.getElementById('timestamp').textContent = new Date().toLocaleString();
    </script>
</body>
</html>
EOF

# Configure basic nginx settings
cat > /etc/nginx/sites-available/default << 'EOF'
server {
    listen 80 default_server;
    listen [::]:80 default_server;

    server_name _;

    root /var/www/html;
    index index.html index.htm index.nginx-debian.html;

    location / {
        try_files $uri $uri/ =404;
    }

    # Enable gzip compression
    gzip on;
    gzip_types text/plain text/css text/javascript;
}
EOF

# Test and reload nginx configuration
nginx -t
systemctl reload nginx

echo "✅ Nginx webserver setup completed successfully"
systemctl status nginx

