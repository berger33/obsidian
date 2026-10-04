---
id: software.seguranca.tranche20.001993
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

# Reproducible Builds: Remover caminhos absolutos e hostnames

## Em uma frase
**Reproducible Builds — Remover caminhos absolutos e hostnames:** Caminhos do workspace e metadados do host podem ser embutidos e tornar binários diferentes.

## Por que importa
O recorte de **remover caminhos absolutos e hostnames** ajuda a permitir que builds independentes comparem resultados e detectem variações ou substituições não explicadas. A equipe registra risco, evidência e responsável.

## Como funciona
Para **remover caminhos absolutos e hostnames**, equipes controlam entradas e fontes de não-determinismo, constroem em ambientes separados e comparam hashes dos artefatos. Delimite entrada e saída. Repita se o alvo mudar.

## Exemplo
Construa em diretórios distintos e use opções de prefix-map suportadas pelo compiler. Teste em staging autorizado.

## Limites e trade-offs
Nem todo gerador ou language tool respeita mesma forma de normalização. Exceções exigem responsável e prazo.

## Como verificar
Compare `strings` ou debug metadata e localize caminho que divergiu. Guarde versão e configuração. Inclua casos positivos e negativos.

## Conexões
- [[reproducible-builds-normalizar-locale-e-timezone]] — Complementa o tópico com reproducible builds: normalizar locale e timezone.

## Fontes
- [Reproducible Builds — SOURCE_DATE_EPOCH](https://reproducible-builds.org/docs/source-date-epoch/) — guia oficial para normalizar timestamp de build e propagá-lo ao ambiente; consultado em 2026-10-04.
- [Linux Kernel — Reproducible builds](https://www.kernel.org/doc/html/latest/kbuild/reproducible-builds.html) — documentação oficial de fontes comuns de não-determinismo e builds reproduzíveis no kernel; consultado em 2026-10-04.
