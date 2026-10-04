---
id: software.seguranca.tranche17.001625
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

# Grype: Atualização e estado da base local

## Em uma frase
**Grype — Atualização e estado da base local:** A correlação depende de dados de vulnerabilidade obtidos e armazenados localmente pelo scanner.

## Por que importa
O recorte de **atualização e estado da base local** ajuda a correlacionar inventário de pacotes com advisories conhecidos e priorizar correções com evidência. A equipe registra risco, evidência e responsável.

## Como funciona
Para **atualização e estado da base local**, recebe uma imagem, diretório ou SBOM, identifica os componentes e compara os resultados com a base local de vulnerabilidades. Delimite entrada e saída. Repita se o alvo mudar.

## Exemplo
Em CI, registre o timestamp e a configuração de atualização da base para cada execução de release. Teste em staging autorizado.

## Limites e trade-offs
Uma base desatualizada pode não conter uma divulgação recente; falha de atualização deve ser visível. Exceções exigem responsável e prazo.

## Como verificar
Verifique logs de atualização e teste o comportamento do pipeline quando a base estiver indisponível. Guarde versão e configuração. Inclua casos positivos e negativos.

## Conexões
- [[grype-triagem-por-severidade-e-contexto]] — Complementa o tópico com grype: triagem por severidade e contexto.

## Fontes
- [Anchore Grype — Repository and Usage](https://github.com/anchore/grype) — repositório oficial com escopos de scan de imagens, sistemas de arquivos e SBOMs; consultado em 2026-10-04.
- [Anchore Grype — Getting Started](https://oss.anchore.com/docs/guides/vulnerability/getting-started/) — guia oficial sobre scans de imagens, diretórios e SBOMs e atualização da base de vulnerabilidades; consultado em 2026-10-04.
