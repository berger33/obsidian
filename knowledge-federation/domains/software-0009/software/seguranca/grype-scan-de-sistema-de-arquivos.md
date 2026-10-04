---
id: software.seguranca.tranche17.001623
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

# Grype: Scan de sistema de arquivos

## Em uma frase
**Grype — Scan de sistema de arquivos:** Diretórios locais podem ser inspecionados sem depender de um artefato OCI final.

## Por que importa
O recorte de **scan de sistema de arquivos** ajuda a correlacionar inventário de pacotes com advisories conhecidos e priorizar correções com evidência. A equipe registra risco, evidência e responsável.

## Como funciona
Para **scan de sistema de arquivos**, recebe uma imagem, diretório ou SBOM, identifica os componentes e compara os resultados com a base local de vulnerabilidades. Delimite entrada e saída. Repita se o alvo mudar.

## Exemplo
Rode Grype no diretório de uma aplicação e compare com o scan da imagem que a pipeline publica. Teste em staging autorizado.

## Limites e trade-offs
Diretório de build pode conter testes ou faltar com dependências instaladas no container. Exceções exigem responsável e prazo.

## Como verificar
Documente o caminho escaneado e confirme diferenças frente ao SBOM da imagem. Guarde versão e configuração. Inclua casos positivos e negativos.

## Conexões
- [[grype-correspondencia-de-ecossistemas-e-versoes]] — Complementa o tópico com grype: correspondência de ecossistemas e versões.

## Fontes
- [Anchore Grype — Repository and Usage](https://github.com/anchore/grype) — repositório oficial com escopos de scan de imagens, sistemas de arquivos e SBOMs; consultado em 2026-10-04.
- [Anchore Grype — Getting Started](https://oss.anchore.com/docs/guides/vulnerability/getting-started/) — guia oficial sobre scans de imagens, diretórios e SBOMs e atualização da base de vulnerabilidades; consultado em 2026-10-04.
