---
id: software.seguranca.tranche05.000482
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
fontes: ["https://gitlab.com/apparmor/apparmor/-/raw/master/README.md", "https://gitlab.com/apparmor/apparmor/-/wikis/home", "https://gitlab.com/apparmor/apparmor/-/wikis/Documentation"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# AppArmor: Modos de Operação de Perfis (`enforce`, `complain`, `unconfined`, `kill`) e Comandos `aa-enforce`, `aa-complain` e `aa-disable`

## Em uma frase
Cada perfil carregado no AppArmor opera em um modo de execução explícito: **`enforce`** (bloqueia qualquer operação não autorizada pelo perfil e registra a violação no log de auditoria) ou **`complain`** (*learning mode* — permite a operação não listada, mas registra `apparmor="ALLOWED"` no `auditd`/`dmesg` para aprendizado).

## Por que importa
Colocar um perfil recém-escrito diretamente em modo `enforce` em produção sem um período de observação em modo `complain` pode interromper fluxos legítimos raros da aplicação (como rotação de certificados ou geração de relatórios mensais).

## Como funciona
Os utilitários de espaço de usuário permitem alternar o modo instantaneamente sem reiniciar o processo confinado: **`sudo aa-complain /etc/apparmor.d/<perfil>`** adiciona a flag `flags=(complain)` e recarrega o perfil; **`sudo aa-enforce /etc/apparmor.d/<perfil>`** ativa o bloqueio estrito; e **`sudo aa-disable /etc/apparmor.d/<perfil>`** cria um symlink em `/etc/apparmor.d/disable/` e descarrega o perfil do kernel.

## Exemplo
```bash
# Colocar o perfil de um servico em modo complain para homologacao e depois promove-lo para enforce
sudo aa-complain /etc/apparmor.d/usr.sbin.nginx
sudo aa-enforce /etc/apparmor.d/usr.sbin.nginx
sudo apparmor_parser -r /etc/apparmor.d/usr.sbin.nginx
```

## Limites e trade-offs
Dentro de um perfil em modo `enforce`, o modificador **`audit`** antes de uma regra (ex.: `audit /etc/ssl/private/** r,`) força o registro de acessos bem-sucedidos, enquanto **`deny`** (ex.: `deny /proc/kcore r,`) bloqueia silenciosamente sem poluir os logs (ou `audit deny` para bloquear e logar mesmo em modo `complain`).

## Como verificar
Verifique com `sudo aa-status` que o binário `/usr/sbin/nginx` e seus workers em execução aparecem listados sob `processes are in enforce mode`.

## Conexões
- [[apparmor-arquitetura-lsm-mandatory-access-control-path-based-profiles]] — Veja também: AppArmor: Arquitetura do Módulo LSM de Controle de Acesso Obrigatório (MAC Baseado em Caminhos e Confinamento de Superusuário).
- [[apparmor-regras-arquivos-capabilities-network-mount-ptrace-signal]] — Veja também: AppArmor: Sintaxe de Regras de Perfil — Permissões de Arquivos (`r`, `w`, `a`, `k`, `l`, `m`), `capability`, `network`, `mount`, `ptrace` e `signal`.
- [[apparmor-geracao-aprendizado-perfis-aa-genprof-aa-logprof-auditd]] — Referência cruzada direta com apparmor-geracao-aprendizado-perfis-aa-genprof-aa-logprof-auditd.

## Fontes
- [AppArmor Official GitLab — Kernel LSM & Userspace Architecture](https://gitlab.com/apparmor/apparmor/-/raw/master/README.md) — documentação oficial do projeto AppArmor cobrindo o módulo LSM do kernel, libapparmor, parser e utilitários; consultado em 2026-10-03.
- [AppArmor Official Wiki — Home & Profiles Overview](https://gitlab.com/apparmor/apparmor/-/wikis/home) — wiki oficial do AppArmor sobre perfis de confinamento, distribuições e ferramentas de política; consultado em 2026-10-03.
- [AppArmor Official Wiki — Technical Documentation](https://gitlab.com/apparmor/apparmor/-/wikis/Documentation) — documentação técnica da linguagem de perfis, transições de execução e abstrações do AppArmor; consultado em 2026-10-03.
