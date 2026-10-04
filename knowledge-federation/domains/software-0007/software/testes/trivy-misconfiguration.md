---
id: software.testes.tranche18.001241
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
fontes: ["https://trivy.dev/latest/docs/scanner/misconfiguration/", "https://trivy.dev/latest/docs/"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Trivy: detectar falhas de configuração

## Em uma frase
O verificador de configuração avalia arquivos de infraestrutura como definições de contêiner, manifestos de orquestração e modelos de provisionamento.

## Por que importa
Problemas de configuração costumam passar das revisões de código e só aparecem em execução, e a análise estática antecipa a detecção.

## Como funciona
Aponte para o diretório de infraestrutura, ajuste as políticas ao contexto do projeto e trate os achados por gravidade.

## Exemplo
Uma definição de contêiner pode executar como usuário privilegiado ou montar diretório sensível, e a análise aponta o trecho responsável.

## Limites e trade-offs
Políticas genéricas geram achados que não se aplicam ao ambiente, e a correção precisa considerar a intenção do manifesto.

## Como verificar
Corrija um achado no manifesto e confirme que ele deixa de aparecer na análise seguinte.

## Conexões
- [[trivy-filesystem-and-repo]] — Veja também: Trivy: analisar sistema de arquivos e repositório.
- [[trivy-secret-scanning]] — Veja também: Trivy: encontrar segredos expostos.

## Fontes
- [Trivy — Misconfiguration scanning](https://trivy.dev/latest/docs/scanner/misconfiguration/) — avaliação de arquivos de infraestrutura contra políticas; consultado em 2026-10-03.
- [Trivy — Documentation](https://trivy.dev/latest/docs/) — alvos, verificadores, políticas, exceções e formatos de saída; consultado em 2026-10-03.
