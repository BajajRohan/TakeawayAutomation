# config file containing test data used in the list api automation workflows
api_key = '6759fa6f94c6a8e33d8d3e15ec2596bf'
base_url = 'https://api.themoviedb.org/4/'
moviedb_ui_url = 'https://www.themoviedb.org'
username = 'rohanbajaj'
# ideally the password should be stored in a secure key vault and read from there, have added it here just for the usage in current project
password = 'tmdb@takeaway2021'
read_access_token = 'eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI2NzU5ZmE2Zjk0YzZhOGUzM2Q4ZDNlMTVlYzI1OTZiZiIsInN1YiI6IjYwMWU3MTFkYzU4YWNkMDA0MWE4MDc3MiIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.McPcldP1XaWaYIlEMRM1V8-DjrcPx8svUiQ6O3nm6JM'
token_headers = {
  'authorization': f'Bearer {read_access_token}',
  'content-type': 'application/json;charset=utf-8'
}
request_token_payload = "{\"redirect_to\":\"http://www.themoviedb.org/\"}"
access_token_payload = "{\"request_token\":\"eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI2NzU5ZmE2Zjk0YzZhOGUzM2Q4ZDNlMTVlYzI1OTZiZiIsImp0aSI6Mjc5NTI4MiwiZXhwIjoxNjEyNjkwMzU2LCJyZWRpcmVjdF90byI6Imh0dHA6Ly93d3cudGhlbW92aWVkYi5vcmcvYXV0aC9hY2Nlc3MvYXBwcm92ZSIsInNjb3BlcyI6WyJwZW5kaW5nX3JlcXVlc3RfdG9rZW4iXSwidmVyc2lvbiI6MSwibmJmIjoxNjEyNjg5NDU2fQ.Vo0vAhCaUNgGrfe_7UbOOpqvnpT8vIfvf_y2kBnA78g\"}"
update_list_payload = "{\"description\":\"Updating list.\"}"
add_item_payload = "{\"items\":[{\"media_type\":\"movie\",\"media_id\":194662},{\"media_type\":\"movie\",\"media_id\":76203},{\"media_type\":\"movie\",\"media_id\":74643}]}"
update_item_payload = "{\"items\":[{\"media_type\":\"movie\",\"media_id\":194662,\"comment\":\"Amazing movie!\"},{\"media_type\":\"movie\",\"media_id\":76203,\"comment\":\"Wow.\"}]}"
