 (cd "$(git rev-parse --show-toplevel)" && git apply --3way <<'EOF' 
diff --git a/README.md b/README.md
index 8b137891791fe96927ad78e64b0aad7bded08bdc..3a6b296e0ca2fdcffd6c424aa127ad1276b43dfe 100644
--- a/README.md
+++ b/README.md
@@ -1 +1,11 @@
+# Open Claw
 
+Run a lightweight demo to visualize and operate the Open Claw interface.
+
+## Run locally
+
+```bash
+python3 open_claw.py --port 8000
+```
+
+Then open [http://localhost:8000](http://localhost:8000) in your browser.
 
EOF
)
