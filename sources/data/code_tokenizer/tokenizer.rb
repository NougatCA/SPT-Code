require "ripper"
require "json"

tokens = Ripper.lex(STDIN).map do |pos, type, str|
  {
    position: {
      line: pos[0],
      column: pos[1]
    },
    type: type.to_s.gsub(/^on_/, ""),
    string: str
  }
end

puts tokens.to_json
