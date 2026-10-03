---
id: software.devops.tranche20.001903
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-devops-2000-0002-tranche-20.md"
fontes: ["https://raw.githubusercontent.com/linuxkit/linuxkit/master/docs/yaml.md", "https://raw.githubusercontent.com/linuxkit/linuxkit/master/README.md", "https://github.com/linuxkit/linuxkit"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# LinuxKit Isolamento de Identidades: alocação automática de `uid` e `gid` por nome de container entre `services` e `files`

## Em uma frase
No LinuxKit, cada container declarado no manifesto YAML recebe automaticamente um identificador numérico único de usuário (`uid`) e de grupo (`gid`), permitindo referenciar o **nome do container** diretamente nos campos `uid:` e `gid:` tanto na definição do serviço quanto na seção `files:`.

## Por que importa
Em imagens de sistema operacional imutáveis construídas a partir de múltiplos containers independentes, coordenar IDs numéricos de usuários manualmente (`1001`, `1002`) entre arquivos de configuração no host e processos dentro dos containers é propenso a erros de permissão.

## Como funciona
Conforme documentado em `docs/yaml.md`, se você declarar um serviço chamado `redis` com `uid: redis` e `gid: redis` e, na seção `files:`, injetar `/etc/redis/redis.conf` também com `uid: redis`, `gid: redis` e `mode: "0600"`, o `linuxkit build` resolve o nome simbólico `redis` para o mesmo ID numérico alocado ao container, garantindo isolamento com menor privilégio sem hardcoding numérico.

## Exemplo
```yaml
services:
  - name: redis
    image: redis:7-alpine
    uid: redis
    gid: redis
    binds:
      - /etc/redis:/etc/redis
files:
  - path: /etc/redis/redis.conf
    contents: "bind 127.0.0.1\nprotected-mode yes\n"
    uid: redis
    gid: redis
    mode: "0600"
```

## Limites e trade-offs
Esse mecanismo permite executar serviços de sistema como usuários não-root dedicados (ou com user namespaces isolados) mantendo a propriedade exata sobre seus arquivos de configuração e certificados montados via `binds`.

## Como verificar
Construa a imagem em formato `tar` (`linuxkit build --format tar file.yml`) e verifique as permissões numéricas atribuídas a `/etc/redis/redis.conf` com `tar -tvf`.

## Conexões
- [[linuxkit-manifesto-yaml-ordem-secoes-kernel-init-onboot-services]] — Veja também: LinuxKit Manifesto YAML (`docs/yaml.md`): ordem de processamento de `kernel`, `init`, `volumes`, `onboot`, `onshutdown`, `services` e `files`.
- [[linuxkit-volumes-blank-filesystem-oci-layout-readonly-mounts]] — Veja também: LinuxKit Seção `volumes`: criação em tempo de build de volumes em branco, `filesystem` populado por imagem e `format: oci`.

## Fontes
- [LinuxKit GitHub — README.md (Toolkit for Building Secure, Portable and Lean Operating Systems for Containers)](https://raw.githubusercontent.com/linuxkit/linuxkit/master/docs/yaml.md) — README oficial do linuxkit/linuxkit apresentando a arquitetura de imagens de SO imutáveis, formatos de saída, plataformas de execução e ferramentas; consultado em 2026-10-03.
- [LinuxKit Official Documentation — YAML Specification (docs/yaml.md: kernel, init, volumes, onboot, onshutdown, services & files)](https://raw.githubusercontent.com/linuxkit/linuxkit/master/README.md) — Especificação oficial YAML do LinuxKit detalhando a ordem de inicialização, alocação simbólica de uid/gid, volumes OCI e configuração runtime; consultado em 2026-10-03.
- [LinuxKit — Official GitHub Repository](https://github.com/linuxkit/linuxkit) — Repositório oficial Apache-2.0 do LinuxKit; consultado em 2026-10-03.
