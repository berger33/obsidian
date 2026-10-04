---
id: software.seguranca.tranche20.001957
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
fontes: ["https://docs.docker.com/scout/", "https://docs.docker.com/scout/explore/analysis/"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# Docker Scout: Distinguir severity e fixability

## Em uma frase
**Docker Scout — Distinguir severity e fixability:** Findings podem variar por severidade e existência de versão corrigida ou recomendação de base.

## Por que importa
O recorte de **distinguir severity e fixability** ajuda a avaliar componentes e risco conhecido de imagens durante desenvolvimento e release. A equipe registra risco, evidência e responsável.

## Como funciona
Para **distinguir severity e fixability**, Scout analisa imagem ou SBOM, correlaciona componentes a vulnerabilidades e apresenta recomendações e políticas. Delimite entrada e saída. Repita se o alvo mudar.

## Exemplo
Priorize crítica corrigível em imagem pública e planeje exceção para dependência sem patch. Teste em staging autorizado.

## Limites e trade-offs
Sem fix disponível não torna vulnerabilidade inofensiva; com fix não garante compatibilidade. Exceções exigem responsável e prazo.

## Como verificar
Verifique versão afetada, versão fixa e origem da recomendação. Guarde versão e configuração. Inclua casos positivos e negativos.

## Conexões
- [[docker-scout-usar-vex-para-comunicar-nao-afetado]] — Complementa o tópico com docker scout: usar vex para comunicar não afetado.

## Fontes
- [Docker Scout — Documentation](https://docs.docker.com/scout/) — documentação oficial de análise, SBOM, vulnerabilities e recomendações; consultado em 2026-10-04.
- [Docker Scout — Explore image analysis](https://docs.docker.com/scout/explore/analysis/) — guia oficial para explorar pacotes, vulnerabilidades e camadas de uma imagem; consultado em 2026-10-04.
