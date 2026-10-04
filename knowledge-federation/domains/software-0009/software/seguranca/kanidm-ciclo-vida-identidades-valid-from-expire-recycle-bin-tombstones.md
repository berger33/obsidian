---
id: software.seguranca.tranche14.001318
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-seguranca-2000-0003-tranche-14.md"
fontes: ["https://raw.githubusercontent.com/kanidm/kanidm/master/README.md", "https://raw.githubusercontent.com/kanidm/kanidm/master/examples/server.toml"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# Governança de Ciclo de Vida de Contas no Kanidm: Janelas Temporais Automáticas (**`--valid-from` / `--expire`**), **Recycle Bin** e **Tombstones**

## Em uma frase
Quantas invasões corporativas acontecem porque a conta de um prestador de serviço temporário, auditor externo ou ex-funcionário continuou ativa meses após o fim do contrato? E o que acontece quando um administrador apaga por acidente um grupo ou usuário importante em produção?

## Por que importa
O Kanidm resolve ambos os problemas nativamente no motor do banco de dados: **(1) Validade Temporal Criptográfica Nativa (`valid_from` e `expire`)** — toda conta de pessoa ou Service Account no Kanidm possui atributos `valid_from` (data/hora RFC 3339 a partir da qual a conta passa a funcionar) e `expire` (data/hora exata em que a conta expira automaticamente!). No exato segundo em que o relógio atinge `expire`, o Kanidm bloqueia logins OIDC, invalida sessões, corta o `Bind` LDAP e **para de entregar as chaves SSH daquela conta nos servidores Linux**, sem depender de nenhum script externo de desprovisionamento!; e **(2) Lixeira Transacional (`Recycle Bin`) e `Tombstones`**!

## Como funciona
Quando você executa `kanidm person delete`, o objeto não desaparece imediatamente: ele vai para a **Recycle Bin** (totalmente inativo), de onde pode ser restaurado intacto com todos os seus UUIDs e vínculos de grupo via **`kanidm recycle-bin revive <nome>`** antes de ser purgado para `Tombstone`!

## Exemplo
```bash
# Definir a janela exata de validade (inicio e expiracao automatica em RFC 3339) de uma conta e listar ou restaurar itens da Recycle Bin
kanidm person validity set prestador.auditoria \
  --from "2026-10-03T08:00:00Z" \
  --until "2026-10-31T23:59:59Z"
kanidm person validity show prestador.auditoria
kanidm recycle-bin list
```

## Limites e trade-offs
Adote como política obrigatória de governança de IAM: **100% das contas de terceiros, consultores, estagiários e contas temporárias de projeto devem nascer com `--until` (`expire`) configurado no ato da criação**!

## Como verificar
E se uma conta for comprometida durante um incidente ativo, rodar **`kanidm person validity expire-at <usuario> now`** corta instantaneamente todos os acessos OIDC, LDAP, RADIUS e SSH do usuário sem apagar os registros forenses da conta.

## Conexões
- [[kanidm-gateway-ldaps-read-only-service-accounts-api-tokens]] — Veja também: Gateway **LDAPS Somente-Leitura (`:636`)** e **Service Accounts** no Kanidm: Integrando Sistemas Legados sem Expor o Diretório a Escritas LDAP.
- [[kanidm-replicacao-alta-disponibilidade-mtls-multi-node-consistencia]] — Veja também: Alta Disponibilidade e **Replicação Multi-Nó (`[replication]`)** no Kanidm: Sincronização via **mTLS** e Resolução de Conflitos por **CSN (*Change Sequence Number*)**.
- [[kanidm-arquitetura-idm-rust-banco-transacional-estrategia-zero-trust]] — Referência cruzada direta com kanidm-arquitetura-idm-rust-banco-transacional-estrategia-zero-trust.
- [[kanidm-integracao-linux-pam-nss-kanidm-unixd-ssh-keys-tpm]] — Referência cruzada direta com kanidm-integracao-linux-pam-nss-kanidm-unixd-ssh-keys-tpm.

## Fontes
- [Kanidm Official GitHub Repository (`kanidm/kanidm`)](https://raw.githubusercontent.com/kanidm/kanidm/master/README.md) — repositório oficial do servidor de gerenciamento de identidade Kanidm em Rust cobrindo WebAuthn/Passkeys, OAuth2/OIDC, LDAPS, RADIUS e clientes POSIX; consultado em 2026-10-03.
- [Kanidm Official Server Configuration Reference (`examples/server.toml`)](https://raw.githubusercontent.com/kanidm/kanidm/master/examples/server.toml) — especificação oficial de configuração do `kanidmd` (`server.toml`) cobrindo `bindaddress`, `ldapbindaddress`, TLS, `domain`, `origin`, `online_backup` e `trust_x_forward_for`; consultado em 2026-10-03.
