require 'cgi'
def display()
  cgi = CGI.new('html4')
  output = cgi.html do
    cgi.head do
      cgi.title { "WHY"}
    end +
    cgi.body do
      cgi.h1 { "OK"}
    end
  end
end
