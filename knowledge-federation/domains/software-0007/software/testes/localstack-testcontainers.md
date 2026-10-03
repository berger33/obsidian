---
id: software.testes.tranche19.001293
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
fontes: ["https://docs.localstack.cloud/aws/tutorials/using-terraform-with-testcontainers-and-localstack/", "https://docs.localstack.cloud/user-guide/integrations/terraform/"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# LocalStack: subir o ambiente dentro do teste

## Em uma frase
A biblioteca de contêineres de teste permite iniciar o serviço emulado durante a execução dos testes, com ciclo de vida controlado pela suíte.

## Por que importa
O ciclo de vida no teste garante isolamento por execução e dispensa ambiente preparado previamente.

## Como funciona
Inicie o contêiner na preparação da suíte, aponte o cliente para o endereço atribuído e descarte ao final.

## Exemplo
Um projeto pode subir o ambiente emulado apenas para as classes de integração, mantendo os testes unitários sem dependência.

## Limites e trade-offs
Subir e derrubar por caso torna a suíte lenta, e contêineres sem descarte explícito vazam recursos entre execuções.

## Como verificar
Meça o tempo da suíte em dois modos de ciclo de vida e confirme que o isolamento se mantém em ambos.

## Conexões
- [[localstack-persistence]] — Veja também: LocalStack: escolher entre estado limpo e persistente.
- [[localstack-terraform-hooks]] — Veja também: LocalStack: usar configuração de infraestrutura como preparação.

## Fontes
- [LocalStack — Terraform e Testcontainers](https://docs.localstack.cloud/aws/tutorials/using-terraform-with-testcontainers-and-localstack/) — preparação automatizada com contêineres de teste; consultado em 2026-10-03.
- [LocalStack — Integração com Terraform](https://docs.localstack.cloud/user-guide/integrations/terraform/) — uso de configuração declarada como preparação do ambiente; consultado em 2026-10-03.
