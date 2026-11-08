from pypdf import PdfReader

pdf = PdfReader("Lab 08 - Salted Hashes.pdf")

page = pdf.pages[0]
annotations = page.get("/Annots", [])

for annotation in annotations:
    obj = annotation.get_object()

    if obj.get("/T") == "Sparky":
        print("=== COMPLETE ANNOTATION ===")
        print(obj)

        print("\n=== APPEARANCE OBJECT ===")
        appearance = obj.get("/AP")

        if appearance:
            normal = appearance.get("/N")
            print(normal.get_object())

            print("\n=== RAW APPEARANCE STREAM ===")
            print(normal.get_object().get_data())