---
id: software.testes.tranche19.001298
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
fontes: ["https://pkg.go.dev/github.com/gruntwork-io/terratest/modules/terraform", "https://github.com/gruntwork-io/terratest"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Terratest: estruturar um teste de infraestrutura

## Em uma frase
O teste é escrito na linguagem de programação do projeto e usa os módulos da biblioteca para inicializar, aplicar e consultar os recursos declarados.

## Por que importa
Verificar a infraestrutura implantada detecta erros que a validação estática da configuração não alcança, como dependências e permissões reais.

## Como funciona
Declare o diretório da configuração, passe as variáveis do teste e execute aplicação e verificação dentro do caso.

## Exemplo
Um teste pode aplicar um módulo de rede e verificar que o identificador do recurso retornado pela saída existe.

## Limites e trade-offs
Testes de infraestrutura são lentos e custam dinheiro, e devem ficar restritos aos fluxos críticos em vez de replicar a suíte toda.

## Como verificar
Execute o teste em ambiente descartável e confirme que os recursos criados correspondem ao que a configuração declara.

## Conexões
- [[terratest-destroy]] — Veja também: Terratest: garantir a destruição dos recursos.

## Fontes
- [Terratest — Módulo terraform](https://pkg.go.dev/github.com/gruntwork-io/terratest/modules/terraform) — opções, aplicação, saídas e destruição; consultado em 2026-10-03.
- [Terratest — repositório oficial](https://github.com/gruntwork-io/terratest) — código-fonte, exemplos e documentação do projeto; consultado em 2026-10-03.
