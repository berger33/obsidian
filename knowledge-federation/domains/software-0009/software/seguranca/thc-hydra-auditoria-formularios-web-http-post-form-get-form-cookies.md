---
id: software.seguranca.tranche16.001573
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-seguranca-2000-0003-tranche-16.md"
fontes: ["https://raw.githubusercontent.com/vanhauser-thc/thc-hydra/master/README", "https://raw.githubusercontent.com/vanhauser-thc/thc-hydra/master/hydra.1"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# Auditando Formulários de Login Web e APIs com **`http-post-form` / `https-post-form`** no THC-Hydra: Sintaxe `"caminho:corpo:condicao"`, `F=` vs. `S=` e Headers `H=`

## Em uma frase
Como funciona a sintaxe de 3 partes separadas por dois-pontos (`:`) do módulo **`http-post-form` (e `https-post-form` / `http-get-form`)** do THC-Hydra para testar formulários de login web que usam `POST` com placeholders **`^USER^`** e **`^PASS^`**?

## Por que importa
O parâmetro de módulo do `http-post-form` tem o formato **`"/url_do_login:corpo_do_post_com_^USER^_e_^PASS^:condicao_de_falha_ou_sucesso"`**!

## Como funciona
Veja os detalhes cruciais da terceira parte (a condição de verificação da resposta HTTP): **(1)** Por padrão (ou prefixando com **`F=`**), a string informa o texto que aparece na página quando o **login FALHA** (ex.: `F= Senha incorreta` ou `F=<div class="error">`); **(2)** Prefixando com **`S=`**, você informa o texto ou cabeçalho que só aparece quando o **login tem SUCESSO** (ex.: `S=302 Found` ou `S=Bem-vindo` ou `S=Location: /dashboard`)! E você pode adicionar uma quarta seção opcional com **`H=Header: Valor`** ou **`c=Cookie`**!

## Exemplo
```bash
# Testar um formulario de login HTTPS POST verificando a condicao de falha (F=) e passando um cabecalho HTTP customizado (H=)
hydra -l admin -P ./senhas_teste.txt -f -t 4 \
  192.0.2.10 https-post-form \
  "/api/login:username=^USER^&password=^PASS^:F=Invalid credentials:H=Content-Type: application/x-www-form-urlencoded"
```

## Limites e trade-offs
E se o corpo do `POST` for um **JSON (`{"user":"^USER^","pass":"^PASS^"}`)** que já contém o caractere dois-pontos (`:`) dentro do JSON? Como o Hydra usa `:` como separador das 3 seções do módulo, se você colocar `:` puro dentro do JSON o parser cortará a string no lugar errado! A solução no Hydra é **escapar os dois-pontos dentro do payload JSON com barra invertida (`\:`)**: ex.: `'{"user"\:"^USER^","pass"\:"^PASS^"}'`!

## Como verificar
Lembre-se também: se o formulário de login exigir um token **CSRF dinâmico** que muda a cada requisição GET antes do POST, ou se você precisar de fuzzing web avançado de múltiplos parâmetros, combine ou prefira o **`ffuf`** que estudamos na Tranche 4.

## Conexões
- [[thc-hydra-modos-credenciais-password-spraying-u-colon-file-e-nsr]] — Veja também: Modos de Credenciais no THC-Hydra: **Password Spraying (`-u` Loop Around Users)**, Pares `login:pass` (**`-C`**), Verificações Extras (**`-e nsr`**) e Parada Imediata (**`-f` / `-F`**).
- [[thc-hydra-controle-concorrencia-tasks-t-timeouts-w-restore-sessao-r]] — Veja também: Controle de Concorrência (**`-t` vs. `-T`**), Pausa Entre Tentativas (**`-W` / `-c`**), Retomada de Sessão (**`-R` `hydra.restore`**) e Saída JSON (**`-b json -o`**) no THC-Hydra.
- [[thc-hydra-arquitetura-auditoria-autenticacao-rede-paralela-modulos]] — Referência cruzada direta com thc-hydra-arquitetura-auditoria-autenticacao-rede-paralela-modulos.

## Fontes
- [THC-Hydra Official Documentation (`vanhauser-thc/thc-hydra/master/README`)](https://raw.githubusercontent.com/vanhauser-thc/thc-hydra/master/README) — documentação oficial do THC-Hydra detalhando protocolos suportados, sintaxe URI `PROTOCOL://TARGET:PORT/OPTIONS`, listas `-M` e inspeção de módulos `hydra -U`; consultado em 2026-10-03.
- [Official `hydra(1)` Manpage Specification (`vanhauser-thc/thc-hydra/master/hydra.1`)](https://raw.githubusercontent.com/vanhauser-thc/thc-hydra/master/hydra.1) — manpage oficial `hydra(1)` detalhando flags `-l`/`-L`, `-p`/`-P`, `-C`, `-e nsr`, `-u`, `-f`/`-F`, `-t`/`-T`, `-w`/`-W`/`-c`, `-R`, `-b json` e o utilitário `pw-inspector`; consultado em 2026-10-03.
