---
id: software.devops.tranche12.001102
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-devops-2000-0002-tranche-12.md"
fontes: ["https://docs.kratix.io/main/quick-start", "https://raw.githubusercontent.com/syntasso/kratix/main/README.md", "https://github.com/syntasso/kratix"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Kratix: Definição de Promise e Contrato de API entre Produtor e Consumidor

## Em uma frase
Uma Promise no Kratix encapsula tanto a definição da API de autoatendimento (`spec.api` contendo uma CRD Kubernetes) quanto os workflows de provisionamento e as dependências de plataforma exigidas para operar um serviço interno em escala.

## Por que importa
Separar claramente o que o consumidor solicita (`spec` enxuto focado na intenção de negócio) do que o produtor de plataforma implementa (operadores, políticas de rede, backups, credenciais) reduz a carga cognitiva sem sacrificar padronização corporativa.

## Como funciona
Ao aplicar um recurso `kind: Promise` (`apiVersion: platform.kratix.io/v1alpha1`), o Kratix valida e instala automaticamente a CRD embutida em `spec.api`, rotulando-a com `kratix.io/promise-name`. O time consumidor passa a consultar o contrato com `kubectl explain` e submeter pedidos declarativos sem precisar conhecer os operadores subjacentes que atendem àquela Promise.

## Exemplo
```bash
kubectl apply -f https://raw.githubusercontent.com/syntasso/promise-postgresql/refs/heads/main/promise.yaml
kubectl get promises.platform.kratix.io
kubectl get crds -l kratix.io/promise-name=postgresql
kubectl explain postgresqls.marketplace.kratix.io.spec
```

## Limites e trade-offs
Expor dezenas de parâmetros de baixo nível do operador subjacente diretamente em `spec.api` da Promise destrói a abstração de plataforma e transfere de volta ao desenvolvedor a complexidade que a IDP deveria absorver.

## Como verificar
Confirme que a Promise entrou em estado `Available` e que `kubectl explain` na CRD gerada exibe descrições claras e defaults seguros para todos os campos opcionais.

## Conexões
- [[kratix-arquitetura-promises-platform-destinations-statestores]] — Veja também: Kratix: Arquitetura com Promises, Platform Cluster, Destinations e State Stores.
- [[kratix-resource-requests-ciclo-vida-status-connectiondetails]] — Veja também: Kratix: Ciclo de Vida de Resource Requests e Retorno de Status ao Consumidor.

## Fontes
- [Kratix GitHub — README.md & Official Quick Start Guide (Promises, Destinations, State Stores & Fleet Management)](https://docs.kratix.io/main/quick-start) — README oficial do syntasso/kratix (Apache-2.0) e guia Quick Start detalhando Promises, Resource Requests, Workflows em containers, State Stores (SeaweedFS/Git), Flux e atualização de frota no Dia 2; consultado em 2026-10-03.
- [Kratix Official Documentation — Quick Start & Platform Concepts](https://raw.githubusercontent.com/syntasso/kratix/main/README.md) — Documentação oficial do Kratix sobre publicação de Promises, status.connectionDetails, Compound Promises e agendamento multi-cluster; consultado em 2026-10-03.
- [Syntasso Kratix — Official GitHub Repository](https://github.com/syntasso/kratix) — Repositório oficial Apache-2.0 do Kratix; consultado em 2026-10-03.
