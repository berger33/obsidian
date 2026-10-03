---
id: software.testes.tranche18.001238
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
fontes: ["https://trivy.dev/latest/docs/", "https://github.com/aquasecurity/trivy"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Trivy: separar alvos e verificadores

## Em uma frase
A ferramenta distingue o que é analisado, como imagem, sistema de arquivos ou configuração, do que é procurado, como vulnerabilidades, segredos ou falhas de configuração.

## Por que importa
Confundir as duas dimensões leva a varreduras que cobrem menos do que se imagina ou que bloqueiam a esteira por ruído.

## Como funciona
Escolha o alvo conforme o artefato disponível e declare os verificadores necessários para a pergunta do momento.

## Exemplo
Uma verificação de revisão pode analisar o sistema de arquivos com verificadores de vulnerabilidade, segredo e configuração, enquanto a imagem construída é analisada após a construção.

## Limites e trade-offs
Executar sem declarar verificadores adicionais deixa segredos e configurações fora do resultado sem aviso claro.

## Como verificar
Compare a saída de uma varredura padrão com outra que declara todos os verificadores e confirme quais categorias passam a aparecer.

## Conexões
- [[trivy-image-scanning]] — Veja também: Trivy: analisar imagens de contêiner.

## Fontes
- [Trivy — Documentation](https://trivy.dev/latest/docs/) — alvos, verificadores, políticas, exceções e formatos de saída; consultado em 2026-10-03.
- [Trivy — repositório oficial](https://github.com/aquasecurity/trivy) — código-fonte, alvos suportados e documentação do projeto; consultado em 2026-10-03.
