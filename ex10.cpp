diff --git a/ex10.cpp b/ex10.cpp
new file mode 100644
index 0000000..5f8e1ca
--- /dev/null
+++ b/ex10.cpp
@@ -0,0 +1,27 @@
+#include<iostream>
+
+using namespace std;
+
+char A[10]="luisa";
+char B[5]="hugo";
+const int sizeA = sizeof(A)/sizeof(A[0]);
+const int sizeB = sizeof(B)/sizeof(B[0]);
+
+
+void copiar(){
+    for(int i = 0 ; A[i] != '\0' ; i++){
+        A[i + sizeB] = B[i];
+    }
+}
+
+void print(){
+    for(int i = 0 ; A[i] != '\0' ; i++){
+        cout<<A[i];
+    }
+}
+
+int main(){
+    copiar();
+    print();
+    return 0;
+}
\ No newline at end of file
