---
id: software.seguranca.tranche17.001682
tipo: tecnica
dominio: software
subdominio: seguranca
nivel: intermediario
confianca: media
ultima_verificacao: 2026-10-04
validade: volatil
status: candidata
revisao_humana: nao_solicitada
revisor: ""
revisao_ia: aprovada
revisor_ia: "Arena.ai Agent Mode"
data_revisao_ia: 2026-10-04
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-seguranca-2000-0003-tranche-17.md"
fontes: ["https://maven.apache.org/enforcer/maven-enforcer-plugin/usage.html#the-enforcer-enforce-mojo", "https://maven.apache.org/enforcer/maven-enforcer-plugin/enforce-mojo.html#fail"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# `fail` no Maven Enforcer: falhar por padrão e tratar warn-only com intenção

## Em uma frase
A configuração documenta `fail` como verdadeiro por padrão, fazendo uma regra reprovada encerrar o goal com falha, salvo política diferente.

## Por que importa
Um perfil permissivo pode deixar mensagens visíveis sem bloquear integração; owners precisam saber se uma regra é aviso ou gate de fato.

## Como funciona
Mantenha falha ativa para requisitos obrigatórios e use modo de aviso somente como migração temporária com prazo e acompanhamento.

## Exemplo
Durante adoção gradual, execute relatório de violações em modo não bloqueante e converta a regra em gate após corrigir os módulos existentes.

```text
mvn enforcer:enforce
```

## Limites e trade-offs
Um goal bem-sucedido não informa regras que não foram configuradas nem garante que o perfil esperado foi ativado naquele build.

## Como verificar
Inspecione configuração efetiva com Maven, force uma violação de teste e confira o status do job e o log gerado.

## Conexões
- [[maven-enforcer-enforce-pipeline-rules-build]] — `maven-enforcer-plugin`: aplicar requisitos de build com regras declaradas.
- [[maven-enforcer-dependency-convergence-transitive-conflicts]] — `dependencyConvergence`: detectar versões transitivas divergentes no grafo Maven.

## Fontes
- [Maven Enforcer — Usage: `fail`](https://maven.apache.org/enforcer/maven-enforcer-plugin/usage.html#the-enforcer-enforce-mojo) — valor padrão e efeito de `fail=false`/nível WARN; consultado em 2026-10-04.
- [Maven Enforcer — parâmetro `fail`](https://maven.apache.org/enforcer/maven-enforcer-plugin/enforce-mojo.html#fail) — default e user property do parâmetro que controla a falha do goal; consultado em 2026-10-04.
