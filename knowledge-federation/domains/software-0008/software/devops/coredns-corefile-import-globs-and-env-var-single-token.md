---
id: software.devops.tranche03.000289
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-devops-2000-0002-tranche-03.md"
fontes: ["https://raw.githubusercontent.com/coredns/coredns/master/README.md", "https://coredns.io/plugins/"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Diretiva import com globs e expansão de variáveis {$VARIABLE} como token único no Corefile

## Em uma frase
Ainda na subseção `Querying CoreDNS`, o README detalha duas regras importantes de sintaxe do `Corefile`: (1) é possível importar outros arquivos de texto para dentro do `Corefile` usando a diretiva `import` (inclusive com globs para casar múltiplos arquivos em uma única diretiva `import`); e (2) variáveis de ambiente podem ser usadas com a sintaxe `{$VARIABLE}`, mas **cada variável de ambiente é inserida no `Corefile` como um único token** (`inserted into the Corefile as a single token`) — isto é, uma variável contendo um espaço será tratada como um único token, e não como dois tokens separados.

## Por que importa
Essa regra do token único evita bugs sutis em produção: se um operador definir `UPSTREAMS="8.8.8.8 1.1.1.1"` e escrever `forward . {$UPSTREAMS}` esperando que o CoreDNS veja dois argumentos separados, o parser tratará a string inteira com espaço como um único token inválido.

## Como funciona
Utilize a diretiva `import` (com globs quando apropriado) para modularizar zonas customizadas em ConfigMaps do Kubernetes e use variáveis `{$VARIABLE}` apenas para valores que representem um único token sintático no `Corefile`.

## Exemplo
Uma plataforma Kubernetes monta arquivos `.server` adicionais via ConfigMap e usa `import /etc/coredns/custom/*.server` no `Corefile` principal para permitir que equipes adicionem zonas de encaminhamento sem editar o bloco principal.

## Limites e trade-offs
Nunca passe múltiplos argumentos separados por espaço dentro de uma única variável `{$ENV_VAR}` no `Corefile`; use variáveis separadas por token ou um arquivo incluído via `import`.

## Como verificar
Conferi a parte final da subseção Querying CoreDNS no README oficial de coredns/coredns.

## Conexões
- [[coredns-default-whoami-behavior-and-dns-port-override]] — Veja também: Comportamento padrão sem Corefile (plugins whoami e log na porta 53) e substituição com -dns.port.
- [[coredns-security-scorecard-and-codeql-verification]] — Veja também: Verificação contínua com CodeQL, Go Tests, CircleCI e OpenSSF Best Practices.

## Fontes
- [CoreDNS — GitHub README](https://raw.githubusercontent.com/coredns/coredns/master/README.md) — Visão geral do CoreDNS (servidor DNS em Go graduado na CNCF baseado em cadeia de plugins, protocolos UDP/TCP/DoT/DoH/DoH3/DoQ/gRPC, 18 capacidades/plugins, compilação com COREDNS_PLUGINS, -log-format=json e regras do Corefile).; consultado em 2026-10-03.
- [CoreDNS Documentation — Built-in Plugins Catalog](https://coredns.io/plugins/) — Catálogo oficial dos plugins in-tree do CoreDNS referenciado no README.; consultado em 2026-10-03.
