---
id: software.seguranca.tranche05.000500
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-seguranca-2000-0003-tranche-05.md"
fontes: ["https://raw.githubusercontent.com/SELinuxProject/selinux/main/README.md", "https://github.com/SELinuxProject/selinux/wiki", "https://github.com/SELinuxProject/selinux/wiki/Tools"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# SELinux: Backup, Replicação Atômica (`semanage export` / `semanage import`) e Automação Idempotente de Políticas em Frota

## Em uma frase
Em ambientes corporativos onde dezenas de servidores compartilham customizações locais de SELinux (booleans ativados, portas adicionadas, contextos `fcontext` e mapeamentos `login`), o utilitário `semanage` permite exportar todas as modificações locais em um único arquivo transacional com **`semanage export`** e aplicá-las atomicamente em outros hosts com **`semanage import`**.

## Por que importa
Invocar `semanage port -a`, `semanage fcontext -a` e `setsebool -P` em 10 comandos separados leva dezenas de segundos porque cada comando reconstrói e recarrega a política binária do `libsemanage`; uma transação única via `semanage import` compila a política **uma única vez** ao final.

## Como funciona
O arquivo gerado por `sudo semanage export -f selinux-local.customizations` contém comandos declarativos (`boolean -m -1 ...`, `port -a ...`, `fcontext -a ...`) que podem ser versionados em Git e aplicados em segundos em novos nós durante o provisionamento automatizado (Packer / Ansible `fedora.linux_system_roles.selinux`).

## Exemplo
```bash
# Exportar todas as customizacoes locais do SELinux para arquivo versionavel e validar importacao transacional
sudo semanage export -f /etc/selinux/local-customizations.semanage
cat /etc/selinux/local-customizations.semanage

# Em um novo servidor provisionado, aplicar todas as customizacoes em uma unica transacao rapida:
sudo semanage import -f /etc/selinux/local-customizations.semanage
```

## Limites e trade-offs
Nota importante: `semanage import` aplica todas as configurações de portas, booleans e regras de `fcontext` no banco do SELinux, mas **não** percorre o disco alterando os inodes existentes; após `semanage import`, execute sempre `sudo restorecon -Rv` nos diretórios customizados.

## Como verificar
Execute `sudo semanage export` em um host configurado e confirme que o arquivo gerado lista exatamente todas as customizações visíveis em `semanage boolean -l -C`, `semanage port -l -C` e `semanage fcontext -l -C`.

## Conexões
- [[selinux-analise-politicas-setools-sesearch-seinfo-auditoria]] — Veja também: SELinux: Auditoria e Consulta Formal da Política Binária com `setools` (`sesearch`, `seinfo` e Desativação Temporária de `dontaudit`).
- [[selinux-arquitetura-mac-baseada-rotulos-type-enforcement-contextos]] — Referência cruzada direta com selinux-arquitetura-mac-baseada-rotulos-type-enforcement-contextos.
- [[selinux-gerenciamento-rotulos-arquivos-semanage-fcontext-restorecon]] — Referência cruzada direta com selinux-gerenciamento-rotulos-arquivos-semanage-fcontext-restorecon.
- [[selinux-gerenciamento-portas-rede-semanage-port-http-ssh]] — Referência cruzada direta com selinux-gerenciamento-portas-rede-semanage-port-http-ssh.

## Fontes
- [SELinuxProject Official GitHub — SELinux Userspace & Policy Toolchain](https://raw.githubusercontent.com/SELinuxProject/selinux/main/README.md) — documentação oficial do SELinux Userspace (libsepol, libselinux, libsemanage, checkpolicy, secilc e versões de política); consultado em 2026-10-03.
- [SELinuxProject Official Wiki — Userspace Tools & Policy Management](https://github.com/SELinuxProject/selinux/wiki) — wiki oficial do SELinux sobre compilação de políticas, semodule, semanage, audit2why e setools; consultado em 2026-10-03.
- [SELinuxProject Official Wiki — Tools Reference](https://github.com/SELinuxProject/selinux/wiki/Tools) — referência das ferramentas oficiais de administração e diagnóstico do SELinux; consultado em 2026-10-03.
