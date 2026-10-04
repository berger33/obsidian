---
id: software.criacao_ia.tranche04.000386
tipo: tecnica
dominio: software
subdominio: criacao-ia
nivel: avancado
confianca: media
ultima_verificacao: 2026-10-04
validade: volatil
status: candidata
revisao_humana: nao_solicitada
revisor: ""
revisao_ia: aprovada
revisor_ia: "Arena.ai Agent Mode"
data_revisao_ia: 2026-10-04
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-criacao-ia-2000-0004-tranche-04.md"
fontes: ["https://github.com/ggml-org/llama.cpp/blob/master/tools/server/README.md", "https://github.com/ggml-org/llama.cpp/blob/master/grammars/README.md"]
tags: [dominio/software, subdominio/criacao-ia, qualidade/candidata]
lote: software-criacao-ia-2000-0004
---

# llama.cpp server: não é um servidor de produção exposto — e as três chaves que aproximam

## Em uma frase
O server traz --api-key (lista CSV, com /health sempre aberta), --timeout (default 3600 s) e --model-log-* etc. como os controles de superfície: a postura da doc é de ferramenta local, não de edge.

## Por que importa
A tentação de 'subir o llama-server na porta 8080 do VPS' é o vetor clássico de RCE-por-prompt e mineração — o server aceita prompts com código, tem /completion irrestrito e, por default, nenhuma auth. As três flags reduzem a superfície mas não a eliminam; o desenho correto mantém o servidor atrás de proxy/rede privada.

## Como funciona
Se a rede exige: --api-key com a lista de chaves válidas (a doc nota explicitamente que /health fica de fora da proteção, para não quebrar health checks — e que a proteção cobre os demais endpoints). --timeout define o teto por request (3600 default na doc) — em exposição pública, baixe-o (3600 s de geração por requisição é um DoS com desconto). --props off (default) mantém o mutation de propriedades no startup; ligá-lo abre POST /props — decisão de rede, não de conveniência. O par completo: bind a 127.0.0.1 por default (a doc registra o comportamento), um nginx/reverse-proxy com auth à frente, e nada de -np gigante para 'segurar os visitantes'.

## Exemplo
Um piloto interno: llama-server em 127.0.0.1:8080, caddy com basic-auth + rate-limit na frente, --timeout 120 e --api-key para os dois clientes conhecidos; /health liberado pro uptime monitor — exatamente o desenho que a postura de 'ferramenta local' da doc sugere como único caminho seguro.

## Limites e trade-offs
API key sem TLS é key em plaintext — a flag não é TLS story, é auth de camada de aplicação. Prompt injection no modelo continua sendo a superfície real mesmo atrás de tudo (o modelo executa o que você mandar gerar, e os endpoints expostos variam por build — confira o README da sua versão, não esta nota). Rate limiting, quotas e billing não existem aqui: são do proxy. E o 503 de /health 'Loading model' com monitor ingênuo pode matar o pod em restart-loop — o health tem que tolerar o load.

## Como verificar
Um scan de portas externo na máquina de teste: /health visível e o resto 401 sem key é o estado esperado da config acima. Rode uma request > timeout e confirme o encerramento com o código esperado (a doc cobre o flag). Teste o POST /props com --props off: deve recusar — e o test é o que prova que o default protege.

## Conexões
- [[llamacpp-endpoints-completion-vs-openai]] — llama.cpp server: /completion é API própria, /v1/completions é a de OpenAI.
- [[gbnf-sintaxe-e-root]] — GBNF: a sintaxe que construi constrangimento de tokens, e o que 'root' significa.

## Fontes
- [llama.cpp — tools/server README](https://github.com/ggml-org/llama.cpp/blob/master/tools/server/README.md) — as flags de api-key (com a nota do /health), timeout e props com seus defaults Consulta: 2026-10-04.
- [llama.cpp — grammars README](https://github.com/ggml-org/llama.cpp/blob/master/grammars/README.md) — o lado de constrained decoding do mesmo binário — exposição abre também o grammar endpoint Consulta: 2026-10-04.
