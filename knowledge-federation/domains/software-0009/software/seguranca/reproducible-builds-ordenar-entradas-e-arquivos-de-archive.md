---
id: software.seguranca.tranche20.001995
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

# Reproducible Builds: Ordenar entradas e arquivos de archive

## Em uma frase
**Reproducible Builds — Ordenar entradas e arquivos de archive:** Ordem de diretório ou archive pode depender do filesystem e produzir hash diferente.

## Por que importa
O recorte de **ordenar entradas e arquivos de archive** ajuda a permitir que builds independentes comparem resultados e detectem variações ou substituições não explicadas. A equipe registra risco, evidência e responsável.

## Como funciona
Para **ordenar entradas e arquivos de archive**, equipes controlam entradas e fontes de não-determinismo, constroem em ambientes separados e comparam hashes dos artefatos. Delimite entrada e saída. Repita se o alvo mudar.

## Exemplo
Defina ordenação determinística ao empacotar fontes e dependências de teste. Teste em staging autorizado.

## Limites e trade-offs
Ordenação de uma etapa não garante que compiladores downstream preservem determinismo. Exceções exigem responsável e prazo.

## Como verificar
Compare listagem interna do archive e hashes em dois workers. Guarde versão e configuração. Inclua casos positivos e negativos.

## Conexões
- [[reproducible-builds-executar-builds-independentes]] — Complementa o tópico com reproducible builds: executar builds independentes.

## Fontes
- [Reproducible Builds — SOURCE_DATE_EPOCH](https://reproducible-builds.org/docs/source-date-epoch/) — guia oficial para normalizar timestamp de build e propagá-lo ao ambiente; consultado em 2026-10-04.
- [Linux Kernel — Reproducible builds](https://www.kernel.org/doc/html/latest/kbuild/reproducible-builds.html) — documentação oficial de fontes comuns de não-determinismo e builds reproduzíveis no kernel; consultado em 2026-10-04.
