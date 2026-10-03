---
id: software.testes.tranche19.001316
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-19.md"
fontes: ["https://github.com/bridgecrewio/checkov/tree/master/checkov/kubernetes", "https://github.com/bridgecrewio/checkov"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Checkov: análise de manifestos de orquestração

## Em uma frase
As verificações de manifestos cobrem segurança de contêineres, limites de recurso, privilégios, redes e controles de escalonamento.

## Por que importa
Manifestos mal configurados expõem cargas de trabalho e nós, e a análise antecipa a correção antes da implantação.

## Como funciona
Rode a análise sobre os manifestos e gráficos do projeto, trate privilégios e limites primeiro e valide as exceções com o time de plataforma.

## Exemplo
Uma carga de trabalho pode exigir execução sem privilégios e sistema de arquivos somente leitura, conforme a verificação aponta.

## Limites e trade-offs
Políticas genéricas podem conflitar com exigências legítimas de plataforma, e exceções amplas por namespace escondem achados reais.

## Como verificar
Aplique a correção em um manifesto e confirme que o achado correspondente desaparece sem afetar a implantação em ambiente de teste.

## Conexões
- [[checkov-terraform-checks]] — Veja também: Checkov: análise de configuração declarada.
- [[checkov-limits-and-practices]] — Veja também: Checkov: reconhecer limites da análise.

## Fontes
- [Checkov — Verificações Kubernetes](https://github.com/bridgecrewio/checkov/tree/master/checkov/kubernetes) — implementação das verificações de manifestos e gráficos; consultado em 2026-10-03.
- [Checkov — repositório oficial](https://github.com/bridgecrewio/checkov) — código-fonte, verificações e documentação do projeto; consultado em 2026-10-03.
