from tkinter import *
from tkinter.filedialog import askopenfilenames, askdirectory
import os
from allProcess import convertDocx2Pdf, convertImage2Pdf, convertPdf2Docx, mergePdfs
from tkinter import messagebox

class App:
    def __init__(self):
        self.root = Tk()
        self.input_paths = []
        self.output_path = None
        self.value_inside = None
        self.selected_option = None
        
        self.rootSetting()

        options = ["Pdf2Word","Word2Pdf","Merge Pdf","Image2Pdf"]
        self.value_inside = StringVar(self.root)
        self.value_inside.set("Select Process")
        options_menu = OptionMenu(self.root, self.value_inside, *options)
        options_menu.place(relx=0.5, rely=0.1, anchor=CENTER)

        self.selectButton = Button(self.root, text="Choose a File", command= lambda : self.selectFiles())
        self.selectButton.place(relx = 0.5, rely = 0.3, anchor=CENTER)

        self.file_label = Label(self.root, text="Selected Files:")
        self.file_label.place(relx = 0.5, rely = 0.4, anchor=CENTER)

        self.outputPathButton = Button(self.root, text="Choose Folder to Save", command= lambda: self.outputDirectory())
        self.outputPathButton.place(relx = 0.5, rely = 0.5, anchor=CENTER)        

        self.outputPathLabel = Label(self.root, text="")
        self.outputPathLabel.place(relx = 0.5, rely = 0.6,anchor=CENTER)

        self.optionButton = Button(self.root, text="Convert", command= lambda : self.checkSelectedOption())
        self.optionButton.place(relx = 0.5, rely = 0.7, anchor=CENTER)

        self.output_label = Label(self.root, text="")
        self.output_label.place(relx = 0.5, rely = 0.8, anchor=CENTER)


        self.root.mainloop()
        

    def rootSetting(self):
        self.root.title("File Converter")
        self.root.geometry('400x400')
        self.root.configure(background="white")
        self.root.resizable(False,False)         

    def selectFiles(self):

        self.selected_option = self.value_inside.get()

        if self.selected_option == "Pdf2Word":
            self.input_paths = list(askopenfilenames(filetypes=[("PDF Files", "*.pdf")]))
            label = ""
            for path in self.input_paths:
                label = f"{label} {self.getFileNameWithType(path)}"
            self.file_label.config(text="Files: " + label)            
        
        elif self.selected_option == "Word2Pdf":
            self.input_paths = list(askopenfilenames(filetypes=[("Doc, Docx Files", "*.doc *.docx")]))
            label = ""
            for path in self.input_paths:
                label = f"{label} {self.getFileNameWithType(path)}"
            self.file_label.config(text="Files: " + label)  

        elif self.selected_option == "Image2Pdf":
            self.input_paths = list(askopenfilenames(filetypes=[("Images", "*.jpg *.jpeg *.png *.gif")]))
            label = ""
            for path in self.input_paths:
                label = f"{label} {self.getFileNameWithType(path)}"
            self.file_label.config(text="Files: " + label)  
        
        elif self.selected_option == "Merge Pdf":
            self.input_paths = list(askopenfilenames(filetypes=[("PDF Files", "*.pdf")]))
            label = ""
            for path in self.input_paths:
                label = f"{label} {self.getFileNameWithType(path)}"
            self.file_label.config(text="Files: " + label)      

        else:
            messagebox.showwarning("Warning","Select a process!")         

    def getFileNameWithType(self,path):
        file_name = os.path.basename(path)
        return file_name
    
    def getFileName(self,path):
        file_name = os.path.basename(path)
        file_name = file_name.split(".")[0]
        return file_name

    def checkSelectedOption(self):

        if len(self.input_paths) == 0:
            messagebox.showerror("Error","Choose a file!")
            return
        self.output_path = f"{self.output_path}/{self.getFileName(self.input_paths[0])}"
        self.selected_option = self.value_inside.get()
        if self.selected_option == "Pdf2Word":
            self.output_path = self.output_path + ".docx"
            convertPdf2Docx(self.input_paths, self.output_path)
            messagebox.showinfo("Successful", "Convert Process Completed!")

        elif self.selected_option == "Word2Pdf":
            self.output_path = self.output_path + ".pdf"
            convertDocx2Pdf(self.input_paths, self.output_path)
            messagebox.showinfo("Successful", "Convert Process Completed!")

        elif self.selected_option == "Merge Pdf":
            self.output_path = self.output_path + ".pdf"
            mergePdfs(self.input_paths, self.output_path)
            messagebox.showinfo("Successful", "Merge Process Completed!")
            
        
        elif self.selected_option == "Image2Pdf":
            self.output_path = self.output_path + ".pdf"
            convertImage2Pdf(self.input_paths, self.output_path)
            messagebox.showinfo("Successful", "Convert Process Completed!")
        
        self.output_label.config(text = self.output_path + " saved.")
        

    def outputDirectory(self):
        self.output_path = askdirectory()
        temp = self.output_path
        # self.output_path = f"{self.output_path}/{self.getFileName(self.input_paths[0])}" #Added file name without type

        self.outputPathLabel.config(text = "Folder: " + temp)
        

app = App()