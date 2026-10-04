---
id: software.seguranca.tranche17.001630
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

# Grype: Diferenciar finding de explorabilidade

## Em uma frase
**Grype — Diferenciar finding de explorabilidade:** Um advisory associado ao componente é um sinal de risco que precisa de avaliação de versão, configuração e fluxo de uso.

## Por que importa
O recorte de **diferenciar finding de explorabilidade** ajuda a correlacionar inventário de pacotes com advisories conhecidos e priorizar correções com evidência. A equipe registra risco, evidência e responsável.

## Como funciona
Para **diferenciar finding de explorabilidade**, recebe uma imagem, diretório ou SBOM, identifica os componentes e compara os resultados com a base local de vulnerabilidades. Delimite entrada e saída. Repita se o alvo mudar.

## Exemplo
Para uma biblioteca em produção, compare o finding com o caminho de chamadas e o VEX aprovado antes de fechar o ticket. Teste em staging autorizado.

## Limites e trade-offs
O scanner não executa aplicação nem demonstra que uma função vulnerável foi alcançada. Exceções exigem responsável e prazo.

## Como verificar
Registre separadamente a correspondência de pacote e a análise de alcançabilidade ou compensação aplicada. Guarde versão e configuração. Inclua casos positivos e negativos.

## Conexões
- [[cosign-assinatura-de-imagem-por-digest]] — Complementa o tópico com sigstore cosign: assinatura de imagem por digest.

## Fontes
- [Anchore Grype — Repository and Usage](https://github.com/anchore/grype) — repositório oficial com escopos de scan de imagens, sistemas de arquivos e SBOMs; consultado em 2026-10-04.
- [Anchore Grype — Getting Started](https://oss.anchore.com/docs/guides/vulnerability/getting-started/) — guia oficial sobre scans de imagens, diretórios e SBOMs e atualização da base de vulnerabilidades; consultado em 2026-10-04.
