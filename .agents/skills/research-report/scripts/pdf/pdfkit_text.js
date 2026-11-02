ObjC.import("PDFKit");
function run(argv) {
  var doc = $.PDFDocument.alloc.initWithURL($.NSURL.fileURLWithPath(argv[0]));
  if (doc.isNil()) return "ERROR: cannot open PDF";
  var n = doc.pageCount, out = [];
  for (var i = 0; i < n; i++) {
    var p = doc.pageAtIndex(i);
    var s = p.isNil() ? "" : p.string;
    out.push("<!-- page " + (i + 1) + " -->\n" + (s.isNil && s.isNil() ? "" : ObjC.unwrap(s)));
  }
  return out.join("\n\n");
}
