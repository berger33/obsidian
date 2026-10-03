---
id: software.seguranca.tranche04.000326
tipo: tecnica
dominio: software
subdominio: seguranca
nivel: intermediario
confianca: media
ultima_verificacao: 2026-10-03
validade: volatil
status: candidata
revisao_humana: nao_solicitada
revisor: ""
revisao_ia: aprovada
revisor_ia: "Arena.ai Agent Mode"
data_revisao_ia: 2026-10-03
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-seguranca-2000-0003-tranche-04.md"
fontes: ["https://raw.githubusercontent.com/presidentbeef/brakeman/main/README.md", "https://raw.githubusercontent.com/presidentbeef/brakeman/main/OPTIONS.md", "https://github.com/presidentbeef/brakeman/tree/main/docs/warning_types"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# Brakeman: Command Injection (`CheckExecute`), SSRF, Path Traversal (`CheckSendFile`) e Dynamic Render

## Em uma frase
O Brakeman audita chamadas de execução de processos (`system`, `exec`, crases `` `...` ``, `Open3`, `Kernel.open`), acesso a arquivos (`send_file`, `File.read`), renderização dinâmica (`render params[:page]`) e redirecionamentos (`redirect_to params[:next]`).

## Por que importa
Em Ruby, `Kernel.open(params[:path])` não apenas permite *Path Traversal*, mas executa comandos de shell arbitrários se o parâmetro começar com um caractere pipe (`|id`); igualmente, `render file: params[:template]` permite leitura e execução de arquivos arbitrários (RCE/LFI).

## Como funciona
As verificações `CheckExecute`, `CheckFileAccess`, `CheckSendFile`, `CheckRender` e `CheckRedirect` rastreiam entradas externas até essas APIs e verificam se há invocação de shell (string única vs múltiplos argumentos em `system("convert", src, dst)`), se `redirect_to` aplica `allow_other_host: false` (padrão no Rails 7+) e se caminhos passam por `File.basename` ou validação estrita.

## Exemplo
```ruby
# INSEGURO — Invoca /bin/sh e permite Command Injection (CheckExecute High):
system("pdftotext #{params[:pdf_name]} output.txt")

# SEGURO — Passa argumentos separados sem shell e restringe o nome do arquivo:
safe_pdf = File.basename(params[:pdf_name].to_s)
system("pdftotext", "--", File.join("/var/uploads", safe_pdf), "/tmp/output.txt")
```

## Limites e trade-offs
Usar `URI.open` (que herda o comportamento legado de `open-uri` em versões antigas) ou construir URLs HTTP internas com parâmetros de usuário permite *Server-Side Request Forgery* (SSRF) contra endpoints de metadados de nuvem (`169.254.169.254`).

## Como verificar
Execute `brakeman -t Execute,FileAccess,SendFile,Render,Redirect` e elimine todas as chamadas de shell por interpolação de string e usos de `Kernel.open`.

## Conexões
- [[brakeman-mass-assignment-strong-parameters-permit-attr-accessible]] — Veja também: Brakeman: Detecção de Mass Assignment e Abuso de Strong Parameters (`permit!` e Chaves Sensíveis).
- [[brakeman-desserializacao-insegura-yaml-marshal-oj-eval-send]] — Veja também: Brakeman: Desserialização Insegura (`YAML.load`, `Marshal.load`, `CSV`), `eval` e `send` Dinâmico.
- [[brakeman-arquitetura-sast-ruby-on-rails-whole-program-ast]] — Referência cruzada direta com brakeman-arquitetura-sast-ruby-on-rails-whole-program-ast.
- [[brakeman-prevencao-sql-injection-activerecord-interpolacao-arel]] — Referência cruzada direta com brakeman-prevencao-sql-injection-activerecord-interpolacao-arel.

## Fontes
- [Brakeman GitHub — README.md (Static Analysis Security Scanner for Ruby on Rails, Confidence Levels, Configuration & CI)](https://raw.githubusercontent.com/presidentbeef/brakeman/main/README.md) — README oficial do presidentbeef/brakeman apresentando a compatibilidade com Rails 2.3 a 8.x, níveis de confiança e uso em CI/CD; consultado em 2026-10-03.
- [Brakeman Official Options Reference — OPTIONS.md (Whole-Program Analysis, Branching, Check Selection, Output Formats & Ignoring Warnings)](https://raw.githubusercontent.com/presidentbeef/brakeman/main/OPTIONS.md) — Referência oficial OPTIONS.md do Brakeman detalhando flags de análise de fluxo, --compare, config/brakeman.ignore e métodos seguros; consultado em 2026-10-03.
- [Brakeman Official Documentation — Warning Types Catalog](https://github.com/presidentbeef/brakeman/tree/main/docs/warning_types) — Catálogo oficial de tipos de vulnerabilidades detectadas pelo Brakeman em aplicações Rails; consultado em 2026-10-03.
