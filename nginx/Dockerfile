FROM nginx:latest

COPY k9174a.conf /etc/nginx

EXPOSE 80 443

CMD ["nginx", "-g", "daemon off;", "-c", "k9174a.conf"]