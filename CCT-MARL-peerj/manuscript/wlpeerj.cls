\NeedsTeXFormat{LaTeX2e}
\ProvidesClass{wlpeerj}[2026/05/27 lightweight PeerJ-style manuscript class]
\LoadClass[10pt,letterpaper]{article}
\RequirePackage[margin=1in]{geometry}
\RequirePackage{authblk}
\RequirePackage{titlesec}
\RequirePackage{xcolor}
\RequirePackage{fancyhdr}
\RequirePackage{abstract}
\RequirePackage{lineno}
\RequirePackage{setspace}
\definecolor{PeerJGreen}{HTML}{4C8C2B}
\definecolor{PeerJBlue}{HTML}{2E6DA4}
\renewcommand\Affilfont{\small\itshape}
\renewcommand\Authfont{\large\bfseries}
\setlength{\affilsep}{0.35em}
\titleformat{\section}{\large\bfseries\color{PeerJGreen}}{}{0pt}{}
\titleformat{\subsection}{\normalsize\bfseries\color{PeerJBlue}}{}{0pt}{}
\titleformat{\subsubsection}{\normalsize\itshape\bfseries}{}{0pt}{}
\titlespacing*{\section}{0pt}{2.2ex plus .5ex minus .2ex}{1.0ex plus .2ex}
\titlespacing*{\subsection}{0pt}{1.5ex plus .3ex minus .2ex}{0.7ex plus .2ex}
\pagestyle{fancy}
\fancyhf{}
\lhead{CCT-MARL for construction coordination}
\rhead{PeerJ Computer Science}
\cfoot{\thepage}
\renewcommand{\headrulewidth}{0.3pt}
\setlength{\parindent}{0.5cm}
\setlength{\parskip}{0pt}
\renewcommand{\baselinestretch}{1.08}
\newcommand{\journalname}{PeerJ Computer Science}
\newcommand{\runningtitle}[1]{\def\@runningtitle{#1}}
\newcommand{\corrauthor}[2][]{\def\@corrauthor{#2}}
\newcommand{\@corrauthor}{}
\newcommand{\keywords}[1]{\def\@keywords{#1}}
\newcommand{\@keywords}{}
\renewenvironment{abstract}{%
  \begin{center}\bfseries Abstract\end{center}%
  \begin{quote}\small
}{%
  \end{quote}
}
\let\oldmaketitle\maketitle
\renewcommand{\maketitle}{%
  \oldmaketitle
  \vspace{-1.0em}
  \ifx\@corrauthor\empty\else
  \begin{center}{\small Corresponding authors: \@corrauthor}\end{center}
  \fi
  \ifx\@keywords\empty\else
  \noindent\textbf{Keywords:} \@keywords\par\vspace{1em}
  \fi
}
