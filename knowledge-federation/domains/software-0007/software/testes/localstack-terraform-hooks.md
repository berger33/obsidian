---
id: software.testes.tranche19.001294
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
fontes: ["https://docs.localstack.cloud/user-guide/integrations/terraform/", "https://docs.localstack.cloud/aws/capabilities/config/initialization-hooks/"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# LocalStack: usar configuração de infraestrutura como preparação

## Em uma frase
Arquivos de infraestrutura podem servir de gancho de inicialização por meio de extensão, criando recursos automaticamente na subida.

## Por que importa
Reaproveitar a mesma infraestrutura declarada aproxima o ambiente de teste do ambiente real e evita script paralelo.

## Como funciona
Monte a configuração declarada, instale a extensão correspondente e execute a preparação quando o serviço estiver pronto.

## Exemplo
O mesmo recurso declarado para produção pode ser aplicado no ambiente emulado durante os testes de integração.

## Limites e trade-offs
Aplicar configuração extensa a cada subida alonga o arranque, e divergências entre versões do provedor mudam o resultado.

## Como verificar
Compare os recursos criados com a lista declarada na configuração e confirme que todos existem antes dos testes.

## Conexões
- [[localstack-testcontainers]] — Veja também: LocalStack: subir o ambiente dentro do teste.
- [[localstack-aws-cli-and-tools]] — Veja também: LocalStack: operar com ferramentas de linha de comando.

## Fontes
- [LocalStack — Integração com Terraform](https://docs.localstack.cloud/user-guide/integrations/terraform/) — uso de configuração declarada como preparação do ambiente; consultado em 2026-10-03.
- [LocalStack — Initialization hooks](https://docs.localstack.cloud/aws/capabilities/config/initialization-hooks/) — fases de inicialização, diretórios e ponto de estado; consultado em 2026-10-03.
