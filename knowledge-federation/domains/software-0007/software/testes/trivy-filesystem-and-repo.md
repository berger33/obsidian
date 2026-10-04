---
id: software.testes.tranche18.001240
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

# Trivy: analisar sistema de arquivos e repositório

## Em uma frase
A varredura pode percorrer diretório local ou repositório remoto, encontrando dependências declaradas, segredos e configurações no código.

## Por que importa
A análise antes da construção detecta problemas cedo, quando a correção é mais barata do que após a publicação do artefato.

## Como funciona
Aponte para o diretório do projeto com os verificadores adequados e integre a execução à revisão de código.

## Exemplo
Uma verificação de revisão pode apontar credencial esquecida em arquivo de configuração antes de ela chegar ao repositório principal.

## Limites e trade-offs
Dependências declaradas sem instalação podem gerar inventário incompleto, e o repositório remoto exige credenciais para projetos privados.

## Como verificar
Compare o resultado da análise do diretório com o da imagem construída e explique as diferenças encontradas.

## Conexões
- [[trivy-image-scanning]] — Veja também: Trivy: analisar imagens de contêiner.
- [[trivy-misconfiguration]] — Veja também: Trivy: detectar falhas de configuração.

## Fontes
- [Trivy — Documentation](https://trivy.dev/latest/docs/) — alvos, verificadores, políticas, exceções e formatos de saída; consultado em 2026-10-03.
- [Trivy — repositório oficial](https://github.com/aquasecurity/trivy) — código-fonte, alvos suportados e documentação do projeto; consultado em 2026-10-03.
