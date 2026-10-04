---
id: software.devops.tranche10.000914
tipo: tecnica
dominio: software
subdominio: devops
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-devops-2000-0002-tranche-10.md"
fontes: ["https://raw.githubusercontent.com/external-secrets/external-secrets/main/README.md", "https://external-secrets.io/latest/introduction/overview/", "https://github.com/external-secrets/external-secrets"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# External Secrets Operator: extração de múltiplas chaves com dataFrom (extract, find e rewrite)

## Em uma frase
Além de mapear chaves uma a uma na lista `spec.data`, o `ExternalSecret` permite importar todas as propriedades de um objeto JSON remoto (`dataFrom.extract`) ou buscar múltiplos segredos por caminho/tags/regex (`dataFrom.find`) aplicando transformações de nomes (`rewrite`).

## Por que importa
Quando um segredo no Vault ou no AWS Secrets Manager guarda um objeto JSON com 25 variáveis de ambiente da aplicação, listar 25 blocos repetitivos em `spec.data` no YAML do `ExternalSecret` gera manutenção desnecessária toda vez que uma variável nova é adicionada no cofre externo.

## Como funciona
Na seção **`spec.dataFrom`** do `ExternalSecret` (mostrada no exemplo da documentação oficial `API Overview`), o operador oferece dois seletores em massa: (1) **`extract`**: recebe `key: <chave-remota>` de um segredo cujo valor no provedor externo é um JSON (ou mapa chave-valor no Vault KV) e transforma automaticamente cada par chave-valor daquele JSON em uma chave individual dentro do `Secret` do Kubernetes; e (2) **`find`**: busca todas as chaves no provedor externo que casam com um caminho (`path`) ou expressão regular (`name.regexp`) ou tags, permitindo encadear regras **`rewrite`** (como `regexp` de substituição) para converter caracteres inválidos em nomes de chaves Kubernetes (ex.: trocando `/` por `_`).

## Exemplo
```yaml
# Extrair todas as chaves de um segredo JSON remoto e reescrever barras '/' para '_' no Secret gerado
apiVersion: external-secrets.io/v1
kind: ExternalSecret
metadata:
  name: app-bulk-env
spec:
  refreshInterval: 1h
  secretStoreRef:
    name: secretstore-sample
    kind: SecretStore
  target:
    name: app-env-secret
  dataFrom:
    - extract:
        key: prod/minha-app/config-json
      rewrite:
        - regexp:
            source: "[^a-zA-Z0-9_-]"
            target: "_"
```

## Limites e trade-offs
Como o Kubernetes restringe estritamente os caracteres permitidos nas chaves de `Secret.data` (permitindo apenas caracteres alfanuméricos, `-`, `_` e `.`), se você usar `dataFrom.find` ou `dataFrom.extract` sobre segredos externos cujos nomes contenham barras (`/`) ou dois-pontos (`:`), a criação do `Secret` no Kubernetes falhará com erro de validação do API Server a menos que você adicione um bloco **`rewrite`** para sanitizar os nomes das chaves.

## Como verificar
Após aplicar o `ExternalSecret` com `dataFrom`, execute `kubectl get secret app-env-secret -o jsonpath='{.data}' | jq 'keys'` para verificar todas as chaves extraídas e renomeadas automaticamente.

## Conexões
- [[externalsecrets-ciclo-reconciliacao-creationpolicy-templates]] — Veja também: External Secrets Operator: ciclo de reconciliação (refreshInterval), creationPolicy e templates de Secret.
- [[externalsecrets-seguranca-rbac-least-privilege-multi-controller]] — Veja também: External Secrets Operator: personas (Cluster Operator vs App Developer), controle de acesso e múltiplos controladores.
- [[externalsecrets-operador-kubernetes-sincronizacao-segredos-externos]] — Referência cruzada direta com externalsecrets-operador-kubernetes-sincronizacao-segredos-externos.
- [[externalsecrets-modelo-recursos-secretstore-externalsecret-clustersecretstore]] — Referência cruzada direta com externalsecrets-modelo-recursos-secretstore-externalsecret-clustersecretstore.

## Fontes
- [External Secrets Operator GitHub — README.md (Supported Providers, CNCF Governance & Release SBOMs)](https://raw.githubusercontent.com/external-secrets/external-secrets/main/README.md) — README oficial do External Secrets Operator (ESO) listando provedores suportados (AWS, Vault, GCP, Azure, IBM, Akeyless, CyberArk, Pulumi ESC) e anexação de SBOM e proveniência; consultado em 2026-10-03.
- [External Secrets Operator Documentation — API Overview (SecretStore, ClusterSecretStore, ExternalSecret, Reconciliation & Access Control)](https://external-secrets.io/latest/introduction/overview/) — Visão geral oficial da arquitetura e modelo de recursos do ESO detalhando SecretStore, ClusterSecretStore, ExternalSecret, ciclo de reconciliação de 5 passos, personas RBAC e múltiplos controladores; consultado em 2026-10-03.
- [External Secrets Operator — Official GitHub Repository](https://github.com/external-secrets/external-secrets) — Repositório oficial Apache-2.0 do projeto external-secrets/external-secrets; consultado em 2026-10-03.
