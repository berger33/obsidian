---
id: software.seguranca.tranche20.001991
tipo: tecnica
dominio: software
subdominio: seguranca
nivel: intermediario
confianca: media
ultima_verificacao: 2026-10-04
validade: volatil
status: candidata
revisao_humana: nao_solicitada
revisor: ""
revisao_ia: aprovada
revisor_ia: "Arena.ai Agent Mode"
data_revisao_ia: 2026-10-04
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-seguranca-2000-0003-tranche-20.md"
fontes: ["https://reproducible-builds.org/docs/source-date-epoch/", "https://www.kernel.org/doc/html/latest/kbuild/reproducible-builds.html"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# Reproducible Builds: Controlar timestamps com SOURCE_DATE_EPOCH

## Em uma frase
**Reproducible Builds — Controlar timestamps com SOURCE_DATE_EPOCH:** SOURCE_DATE_EPOCH permite derivar timestamp de build de uma fonte estável em vez do relógio atual.

## Por que importa
O recorte de **controlar timestamps com source_date_epoch** ajuda a permitir que builds independentes comparem resultados e detectem variações ou substituições não explicadas. A equipe registra risco, evidência e responsável.

## Como funciona
Para **controlar timestamps com source_date_epoch**, equipes controlam entradas e fontes de não-determinismo, constroem em ambientes separados e comparam hashes dos artefatos. Delimite entrada e saída. Repita se o alvo mudar.

## Exemplo
Use timestamp de commit em dois builds do mesmo release de teste. Teste em staging autorizado.

## Limites e trade-offs
Ferramentas podem ignorar variável ou produzir outro timestamp por arquivo. Exceções exigem responsável e prazo.

## Como verificar
Compare metadados e arquivos do artefato antes e depois de fixar o tempo. Guarde versão e configuração. Inclua casos positivos e negativos.

## Conexões
- [[reproducible-builds-fixar-toolchain-e-dependencias]] — Complementa o tópico com reproducible builds: fixar toolchain e dependências.

## Fontes
- [Reproducible Builds — SOURCE_DATE_EPOCH](https://reproducible-builds.org/docs/source-date-epoch/) — guia oficial para normalizar timestamp de build e propagá-lo ao ambiente; consultado em 2026-10-04.
- [Linux Kernel — Reproducible builds](https://www.kernel.org/doc/html/latest/kbuild/reproducible-builds.html) — documentação oficial de fontes comuns de não-determinismo e builds reproduzíveis no kernel; consultado em 2026-10-04.
