---
id: software.testes.tranche18.001243
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-18.md"
fontes: ["https://trivy.dev/latest/docs/supply-chain/sbom/", "https://trivy.dev/latest/docs/"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Trivy: gerar e consumir inventário de software

## Em uma frase
A ferramenta produz inventário em formatos padronizados a partir de imagens e sistemas de arquivos, e também analisa inventários existentes.

## Por que importa
O inventário descreve os componentes do artefato, permitindo reavaliar vulnerabilidades depois, sem reconstruir a imagem.

## Como funciona
Gere o inventário como artefato da construção, versione-o junto da imagem e use-o para reanálises periódicas.

## Exemplo
Um inventário publicado permite consultar meses depois quais versões de biblioteca estavam presentes em uma imagem específica.

## Limites e trade-offs
Inventários sem vínculo claro com a imagem perdem utilidade, e formatos não padronizados dificultam o consumo por outras ferramentas.

## Como verificar
Gere o inventário, analise-o em seguida e confirme que os componentes listados coincidem com os da imagem.

## Conexões
- [[trivy-secret-scanning]] — Veja também: Trivy: encontrar segredos expostos.
- [[trivy-ignore-and-baseline]] — Veja também: Trivy: registrar exceções com validade.

## Fontes
- [Trivy — SBOM](https://trivy.dev/latest/docs/supply-chain/sbom/) — geração e análise de inventário de software em formatos padronizados; consultado em 2026-10-03.
- [Trivy — Documentation](https://trivy.dev/latest/docs/) — alvos, verificadores, políticas, exceções e formatos de saída; consultado em 2026-10-03.
