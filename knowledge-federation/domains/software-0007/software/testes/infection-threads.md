---
id: software.testes.tranche23.001744
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-23.md"
fontes: ["https://infection.github.io/guide/command-line-options.html", "https://infection.github.io/guide/"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# --threads: paralelismo primeiro, depois benchmark

## Em uma frase
A seção de threads da doc oficial de opções prescreve --threads (ou -j) maior que 1 para rodar os testes dos códigos mutados em paralelo — "it will dramatically speed up mutation process" — e documenta o --threads=max para autodetecção de cores, além do receituário antigo para versões < 0.26.15 (infection -j$(nproc) no Linux, $(sysctl -n hw.ncpu) no macOS).

## Por que importa
A frase que deve colar no cartaz é a ressalva: se os seus testes dependem entre si ou usam banco de dados, paralelismo "can lead to failing tests which give many false-positives results" — falsos kills: mutante declarado morto porque o teste concorrente quebrar, não porque a asserção pegou a mudança.

## Como funciona
A página ainda quebra o mito de monotonicidade: "running Infection with more threads does not necessarily lead to better performance", com a prescrição explícita de benchmarcar vários valores para o seu caso.

## Exemplo
Comece com --threads=4 como no exemplo da instalação; suba até o dobro dos cores lógicos e compare o tempo total e o volume de killed por timeout/erro anormal — uma inflação de erros entre configurações denuncia o false-positive documentado.

## Limites e trade-offs
A doc não define isolamento de recursos por worker (memória, handles de banco) — o limite útil de threads é função da sua árvore de testes, não do número do flags; em CI compartilhado o max teórico costuma ser justamente o caso de erro da ressalva.

## Como verificar
Abra a seção --threads da página Command line options e confirme as três frases citadas (dramatically, false-positives, benchmarking).

## Conexões
- [[infection-install-phar]] — Veja também: Instalar o phar assinado: GPG, phive, composer e brew.
- [[infection-reuse-coverage]] — Veja também: Reusar cobertura existente em vez de gerar de novo.

## Fontes
- [Infection — Command line options](https://infection.github.io/guide/command-line-options.html) — threads, test-framework, coverage, git-diff e loggers; consultado em 2026-10-03.
- [Infection — Introduction do guia oficial](https://infection.github.io/guide/) — mutation testing, os cinco passos, métricas MSI/MCC e playground; consultado em 2026-10-03.
