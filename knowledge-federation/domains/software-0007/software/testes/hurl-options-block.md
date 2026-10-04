---
id: software.testes.tranche16.001050
tipo: tecnica
dominio: software
subdominio: testes
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-16.md"
fontes: ["https://hurl.dev/docs/hurl-file.html", "https://hurl.dev/docs/manual.html"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Hurl: configurar comportamento por entrada

## Em uma frase
O bloco de opções permite declarar por entrada ajustes como repetição com intervalo, atraso entre requisições e política de continuidade após erro.

## Por que importa
Ajustes locais mantêm o arquivo autossuficiente e deixam claro que a repetição faz parte do fluxo, não do ambiente de execução.

## Como funciona
Declare as opções no bloco próprio da entrada, informe os valores necessários e evite depender de configuração externa para o comportamento essencial do caso.

## Exemplo
Uma espera por recurso que passa por assíncrono pode usar repetição com intervalo até que a asserção seja satisfeita.

## Limites e trade-offs
A repetição só é interrompida pelo sucesso da verificação, e a ausência dela faz o arquivo falhar por condição ainda não atendida.

## Como verificar
Ative a repetição em um cenário com atraso conhecido e confirme que a execução é bem-sucedida depois de algumas tentativas.

## Conexões
- [[hurl-status-and-error-handling]] — Veja também: Hurl: tratar códigos de status e falhas.
- [[hurl-cli-test-mode]] — Veja também: Hurl: executar vários arquivos em paralelo.

## Fontes
- [Hurl — File format](https://hurl.dev/docs/hurl-file.html) — estrutura de entradas, resposta esperada, opções e escopo de sessão; consultado em 2026-10-03.
- [Hurl — Manual (CLI)](https://hurl.dev/docs/manual.html) — modo de teste, paralelismo, repetição, relatórios e códigos de saída; consultado em 2026-10-03.
