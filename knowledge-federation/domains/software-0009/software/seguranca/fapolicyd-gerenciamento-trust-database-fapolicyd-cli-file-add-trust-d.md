---
id: software.seguranca.tranche15.001434
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-seguranca-2000-0003-tranche-15.md"
fontes: ["https://raw.githubusercontent.com/linux-application-whitelisting/fapolicyd/main/README.md", "https://raw.githubusercontent.com/linux-application-whitelisting/fapolicyd/main/init/fapolicyd.conf"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# Gerenciando o **Banco de Confiança (`trust.d/`)** com **`fapolicyd-cli`**: Autorizando Binários Customizados, Agentes de Terceiros e Aplicações em `/opt`

## Em uma frase
Em todo servidor corporativo real, além dos pacotes instalados via `rpm`/`dpkg`, você frequentemente possui alguns binários legítimos instalados em `/opt/` ou `/usr/local/bin/` (por exemplo, um agente de monitoramento interno ou uma aplicação compilada em Go/Rust pela própria empresa). Como cadastrar esses arquivos no **Banco de Confiança (`Trust Database`)** do `fapolicyd` para que eles tenham `trust=1` sem afrouxar a política de segurança?

## Por que importa
Usando o utilitário **`fapolicyd-cli --file add`** (que grava entradas organizadas dentro do diretório **`/etc/fapolicyd/trust.d/`** ou `/etc/fapolicyd/fapolicyd.trust`) seguido de **`fapolicyd-cli --update`**!

## Como funciona
Quando você executa **`fapolicyd-cli --file add /opt/minha-app/bin/servidor --trust-file minha-app`**, o `fapolicyd-cli` calcula automaticamente o **tamanho exato em bytes** e o **hash criptográfico `SHA-256`** de `/opt/minha-app/bin/servidor` (ou de todos os arquivos dentro de um diretório se você passar uma pasta!) e grava no arquivo `/etc/fapolicyd/trust.d/minha-app`!

## Exemplo
```bash
# Adicionar uma aplicacao corporativa em /opt/app-pagamentos/ ao banco de confianca (/etc/fapolicyd/trust.d/app-pagamentos) e atualizar o daemon a quente
fapolicyd-cli --file add /opt/app-pagamentos/bin/ --trust-file app-pagamentos
cat /etc/fapolicyd/trust.d/app-pagamentos
fapolicyd-cli --update
```

## Limites e trade-offs
O que acontece se você atualizar o binário `/opt/app-pagamentos/bin/worker` durante um deploy de nova versão da aplicação e esquecer de atualizar o hash no `trust.d/app-pagamentos`? Se a verificação de integridade estiver ativa (`integrity = sha256` ou `size`), o tamanho/hash do novo binário não baterá com o registrado no banco LMDB! Para atualizar automaticamente os tamanhos e hashes `SHA-256` de todos os arquivos listados em `/etc/fapolicyd/trust.d/app-pagamentos` após um deploy autorizado, basta adicionar no seu playbook de deploy: **`fapolicyd-cli --file update /opt/app-pagamentos/bin/ --trust-file app-pagamentos && fapolicyd-cli --update`**!

## Como verificar
Use **`fapolicyd-cli --check-trustdb`** regularmente para auditar se algum arquivo listado no banco de confiança foi modificado no disco ou removido.

## Conexões
- [[fapolicyd-sintaxe-regras-decision-perm-subject-object-customizacao]] — Veja também: A Receita de Escrita de Regras no fapolicyd: **`decision perm subject : object`**, Tipos MIME (`ftype`), `trust=1` e `deny_audit`.
- [[fapolicyd-verificacao-integridade-sha256-size-ima-anti-tampering]] — Veja também: Modos de Verificação de Integridade (**`integrity = none | size | ima | sha256`**) no `/etc/fapolicyd/fapolicyd.conf`: Impedindo Substituição de Binários Confiáveis!.
- [[fapolicyd-arquitetura-application-whitelisting-fanotify-rpmdb-lmdb]] — Referência cruzada direta com fapolicyd-arquitetura-application-whitelisting-fanotify-rpmdb-lmdb.

## Fontes
- [Official `fapolicyd` GitHub Repository (`linux-application-whitelisting/fapolicyd`)](https://raw.githubusercontent.com/linux-application-whitelisting/fapolicyd/main/README.md) — repositório oficial do File Access Policy Daemon cobrindo interceptação de execução via `fanotify`, linguagem de regras `allow`/`deny_audit`, `fapolicyd-cli` e banco de confiança; consultado em 2026-10-03.
- [Official `fapolicyd.conf` Configuration Specification (`init/fapolicyd.conf`)](https://raw.githubusercontent.com/linux-application-whitelisting/fapolicyd/main/init/fapolicyd.conf) — especificação oficial de configuração do `/etc/fapolicyd/fapolicyd.conf` detalhando `permissive`, `trust = rpmdb,file`, `integrity = none|size|ima|sha256`, `watch_fs` e caches LRU; consultado em 2026-10-03.
