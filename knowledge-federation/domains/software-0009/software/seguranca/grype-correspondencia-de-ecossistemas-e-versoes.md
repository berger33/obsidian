---
id: software.seguranca.tranche17.001624
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-seguranca-2000-0003-tranche-17.md"
fontes: ["https://github.com/anchore/grype", "https://oss.anchore.com/docs/guides/vulnerability/getting-started/"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# Grype: Correspondência de ecossistemas e versões

## Em uma frase
**Grype — Correspondência de ecossistemas e versões:** A identificação de ecossistema e versão condiciona quais advisories podem ser associados a um componente.

## Por que importa
O recorte de **correspondência de ecossistemas e versões** ajuda a correlacionar inventário de pacotes com advisories conhecidos e priorizar correções com evidência. A equipe registra risco, evidência e responsável.

## Como funciona
Para **correspondência de ecossistemas e versões**, recebe uma imagem, diretório ou SBOM, identifica os componentes e compara os resultados com a base local de vulnerabilidades. Delimite entrada e saída. Repita se o alvo mudar.

## Exemplo
Use uma dependência de laboratório com versão vulnerável conhecida para conferir nome, versão e identificador de advisory. Teste em staging autorizado.

## Limites e trade-offs
Metadados vagos, forks e versões customizadas podem gerar matches incertos ou deixar o advisory sem correlação. Exceções exigem responsável e prazo.

## Como verificar
Revise os campos do pacote e a regra de correspondência antes de automatizar bloqueios. Guarde versão e configuração. Inclua casos positivos e negativos.

## Conexões
- [[grype-atualizacao-e-estado-da-base-local]] — Complementa o tópico com grype: atualização e estado da base local.

## Fontes
- [Anchore Grype — Repository and Usage](https://github.com/anchore/grype) — repositório oficial com escopos de scan de imagens, sistemas de arquivos e SBOMs; consultado em 2026-10-04.
- [Anchore Grype — Getting Started](https://oss.anchore.com/docs/guides/vulnerability/getting-started/) — guia oficial sobre scans de imagens, diretórios e SBOMs e atualização da base de vulnerabilidades; consultado em 2026-10-04.
