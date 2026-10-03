---
id: software.testes.tranche24.001794
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-24.md"
fontes: ["https://raw.githubusercontent.com/google/honggfuzz/master/README.md", "https://github.com/google/honggfuzz/blob/master/docs/USAGE.md"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# ptrace: detectar sinais sequestrados e crashes escondidos

## Em uma frase
O README lista "Deep Monitoring: Uses low-level APIs (ptrace) to detect hijacked signals and hidden crashes" — a observação do processo fuzzado é feita em nível de ptrace, capturando situações em que o handler de sinal do próprio alvo engole a falha que o fuzzador deveria ver.

## Por que importa
A classe de bug mais traiçoeira em fuzzing é a que não derruba o processo: crash transformado em return silencioso por um handler catch-all. Monitorar via ptrace tira essa decisão das mãos do alvo — o detector fica fora do alcance do código testado.

## Como funciona
Rode o alvo sem mudanças no tratamento de sinais e deixe o monitor do Honggfuzz observar o processo; a detecção de crash independe de o alvo instalar handlers, porque o sinal é visto pela API de baixo nível antes do tratamento interno.

## Exemplo
Um parser que chama exit(0) dentro do handler de SIGSEGV ainda aparece como crash para o processo de monitoramento descrito no README.

## Limites e trade-offs
Os mecanismos internos de classificação (quais sinais contam, timeouts) não são detalhados no README; USAGE.md linkado é onde o comportamento fino é especificado.

## Como verificar
A linha de "Deep Monitoring" do bloco Key Features do README oficial descreve exatamente esse mecanismo.

## Conexões
- [[honggfuzz-empty-corpus]] — Veja também: Começar do zero: corpus vazio que se auto-constrói.
- [[honggfuzz-platform-support]] — Veja também: Seis famílias de SO: do Linux ao Windows via Cygwin.

## Fontes
- [Honggfuzz — README oficial](https://raw.githubusercontent.com/google/honggfuzz/master/README.md) — README oficial do Honggfuzz com recursos de cobertura por hardware/software, modo persistente, ptrace, build wrappers, placeholder ___FILE___ e trophies.; consultado em 2026-10-03.
- [Honggfuzz — USAGE.md no repositório oficial](https://github.com/google/honggfuzz/blob/master/docs/USAGE.md) — Documento oficial USAGE.md do Honggfuzz com opções detalhadas de execução, cobertura e monitoramento.; consultado em 2026-10-03.
