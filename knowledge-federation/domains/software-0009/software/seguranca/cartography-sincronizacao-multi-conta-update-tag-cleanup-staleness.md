---
id: software.seguranca.tranche11.001009
tipo: tecnica
dominio: software
subdominio: seguranca
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-seguranca-2000-0003-tranche-11.md"
fontes: ["https://raw.githubusercontent.com/cartography-cncf/cartography/master/README.md", "https://docs.cartography.dev/usage/tutorial.html"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# Operação em Produção do Cartography: Sincronização Multi-Conta AWS (`--aws-sync-all-profiles`), **`UPDATE_TAG`** e Limpeza de Nós Obsoletos (**`Cleanup Jobs`**)

## Em uma frase
Como o Cartography mantém o grafo Neo4j fiel ao estado atual da nuvem quando instâncias EC2, Pods Kubernetes e containers são criados e destruídos a cada minuto?

## Por que importa
A resposta está no mecanismo de **Marcação Temporal de Sincronização (`UPDATE_TAG` / `lastupdated`)** e nos **Cleanup Jobs**: no início de uma execução do `cartography`, um timestamp Unix único (`update_tag`) é gerado; cada nó e cada aresta criados ou confirmados durante aquela execução recebem a propriedade **`lastupdated = update_tag`**!

## Como funciona
Ao final da sincronização de cada módulo, o Cartography executa os **Cleanup Jobs**, que removem automaticamente do Neo4j todos os nós e relacionamentos daquele escopo cujo `lastupdated` seja **anterior ao `update_tag` atual** (ou seja, recursos que deixaram de existir na nuvem desde o último sync!), evitando que o grafo acumule "recursos fantasmas" (*stale nodes*)!

## Exemplo
```bash
# Sincronizar todas as contas AWS configuradas nos perfis locais (--aws-sync-all-profiles) registrando metricas StatsD
export AWS_CONFIG_FILE=/etc/cartography/aws_config
export NEO4J_PASSWORD="senha-segura-neo4j-prod"

cartography \
  --neo4j-uri bolt://neo4j.secops.internal:7687 \
  --neo4j-user neo4j \
  --neo4j-password-env-var NEO4J_PASSWORD \
  --selected-modules aws \
  --aws-sync-all-profiles \
  --aws-requested-syncs ec2:instance,ec2:security_group,s3,iam,rds,eks \
  --statsd-enabled \
  --statsd-host 127.0.0.1
```

## Limites e trade-offs
Observe a flag **`--aws-requested-syncs`** no exemplo acima: em contas gigantescas onde você precisa atualizar dados voláteis (como `ec2:instance`, `ec2:security_group` e `s3`) a cada hora, você pode rodar um job rápido apenas com os sub-módulos desejados e deixar um job completo noturno para sincronizar todos os 30+ serviços!

## Como verificar
Monitore as métricas emitidas via `--statsd-enabled` para acompanhar a duração de cada estágio e detectar falhas de permissão IAM (`AccessDenied`) em contas-membro.

## Conexões
- [[cartography-governanca-ia-agentes-bedrock-vertex-openai-anthropic-aibom]] — Veja também: Segurança e Governança de **IA em Produção (`AI Security Posture / AIBOM`)** no Cartography: **AWS Bedrock, GCP Vertex AI, OpenAI e Anthropic**.
- [[cartography-extensibilidade-custom-modules-drift-detection-auditoria]] — Veja também: Extensibilidade do Cartography: Como Construir **Módulos Customizados (`IntelModule`)** para Ingerir Ativos Internos e CMDBs no Grafo de Segurança.
- [[cartography-arquitetura-grafo-neo4j-ativos-multi-cloud-cncf]] — Referência cruzada direta com cartography-arquitetura-grafo-neo4j-ativos-multi-cloud-cncf.
- [[cloudquery-modos-sincronizacao-write-mode-overwrite-delete-stale-append]] — Referência cruzada direta com cloudquery-modos-sincronizacao-write-mode-overwrite-delete-stale-append.
- [[steampipe-agregadores-multi-conta-connections-spc-aws-organizations]] — Referência cruzada direta com steampipe-agregadores-multi-conta-connections-spc-aws-organizations.

## Fontes
- [CNCF Cartography Official GitHub — Multi-Platform Infrastructure & Identity Graph in Neo4j](https://raw.githubusercontent.com/cartography-cncf/cartography/master/README.md) — repositório oficial do CNCF Cartography cobrindo os 30+ módulos suportados (AWS, GCP, Azure, K8s, Okta, Entra ID, GitHub, CrowdStrike, AIBOM) e `cartography-rules`; consultado em 2026-10-03.
- [CNCF Cartography Official Documentation — Querying Tutorial & Data Enrichment (`exposed_internet`, `anonymous_access`)](https://docs.cartography.dev/usage/tutorial.html) — documentação oficial do Cartography demonstrando consultas OpenCypher e enriquecimento automático de superfície de ataque no Neo4j; consultado em 2026-10-03.
