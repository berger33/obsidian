---
id: software.seguranca.tranche20.001958
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

# Docker Scout: Usar VEX para comunicar não afetado

## Em uma frase
**Docker Scout — Usar VEX para comunicar não afetado:** Dados VEX relacionados podem fornecer contexto sobre vulnerabilidades sem alterar SBOM base.

## Por que importa
O recorte de **usar vex para comunicar não afetado** ajuda a avaliar componentes e risco conhecido de imagens durante desenvolvimento e release. A equipe registra risco, evidência e responsável.

## Como funciona
Para **usar vex para comunicar não afetado**, Scout analisa imagem ou SBOM, correlaciona componentes a vulnerabilidades e apresenta recomendações e políticas. Delimite entrada e saída. Repita se o alvo mudar.

## Exemplo
Associe justificativa VEX específica ao digest e CVE após análise de impacto. Teste em staging autorizado.

## Limites e trade-offs
VEX desatualizado ou amplo pode silenciar finding aplicável a outra versão. Exceções exigem responsável e prazo.

## Como verificar
Confira produto, versão, status e evidência antes de usar documento VEX. Guarde versão e configuração. Inclua casos positivos e negativos.

## Conexões
- [[docker-scout-controlar-credenciais-ao-analisar-registry]] — Complementa o tópico com docker scout: controlar credenciais ao analisar registry.

## Fontes
- [Docker Scout — Documentation](https://docs.docker.com/scout/) — documentação oficial de análise, SBOM, vulnerabilities e recomendações; consultado em 2026-10-04.
- [Docker Scout — Explore image analysis](https://docs.docker.com/scout/explore/analysis/) — guia oficial para explorar pacotes, vulnerabilidades e camadas de uma imagem; consultado em 2026-10-04.
