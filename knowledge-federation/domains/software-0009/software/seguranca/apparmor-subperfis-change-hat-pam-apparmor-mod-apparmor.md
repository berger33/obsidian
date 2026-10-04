---
id: software.seguranca.tranche05.000488
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

# AppArmor: Mudança Dinâmica de Privilégio Intra-Processo com `aa_change_hat(2)`, `aa_change_profile(2)` e `pam_apparmor`

## Em uma frase
A biblioteca **`libapparmor`** (licenciada sob LGPL) expõe as chamadas de API **`aa_change_hat()`** e **`aa_change_profile()`**, utilizadas por módulos como `mod_apparmor` (Apache) e `pam_apparmor` (PAM) para alterar o confinamento de um processo já em execução sem precisar invocar `execve()`.

## Por que importa
Um servidor web multi-tenant ou um daemon de sessão SSH inicia com privilégios mais amplos, mas assim que identifica qual virtual host HTTP ou qual usuário PAM autenticou, pode restringir aquela thread/processo específico a um subperfil (**`^hat`**) muito mais restrito.

## Como funciona
Com `aa_change_profile()`, a transição é unidirecional e irreversível (o processo nunca mais pode voltar ao perfil original). Já com `aa_change_hat(subprofile, magic_token)`, o processo passa um token secreto aleatório de 64 bits ao kernel para entrar no subperfil `^subprofile` durante o processamento da requisição e pode fornecer o mesmo `magic_token` ao final para retornar ao perfil pai.

## Exemplo
```nginx
profile /usr/sbin/apache2 {
  #include <abstractions/base>
  #include <abstractions/apache2-common>

  # Subperfil (Hat) dedicado exclusivamente ao VirtualHost de upload de documentos
  ^vhost_uploads {
    #include <abstractions/base>
    /var/www/uploads/** rw,
    deny /var/www/admin/** rwx,
    deny /bin/** x,
  }
}
```

## Limites e trade-offs
Se o processo dentro do `^hat` for comprometido por um exploit de corrupção de memória (buffer overflow) na mesma thread onde o `magic_token` está armazenado na heap/stack, o atacante poderia ler o token da memória e chamar `aa_change_hat(NULL, magic_token)`; para isolamento definitivo, prefira processos separados com **`aa_change_profile()`** (irreversível).

## Como verificar
Inspecione `sudo aa-status` e confirme que os subperfis `apache2//vhost_uploads` estão carregados no kernel.

## Conexões
- [[apparmor-integracao-containers-docker-kubernetes-securitycontext]] — Veja também: AppArmor: Confinamento de Containers e Pods Kubernetes (`securityContext.appArmorProfile` GA no Kubernetes v1.30+).
- [[apparmor-diagnostico-violacoes-apparmor-denied-dmesg-ausearch]] — Veja também: AppArmor: Diagnóstico de Negativas (`apparmor="DENIED"`), `aa-notify` e Decodificação de Campos `operation`, `requested_mask` e `denied_mask`.
- [[apparmor-arquitetura-lsm-mandatory-access-control-path-based-profiles]] — Referência cruzada direta com apparmor-arquitetura-lsm-mandatory-access-control-path-based-profiles.
- [[apparmor-transicoes-execucao-ix-px-cx-ux-scrubbing-ambiente]] — Referência cruzada direta com apparmor-transicoes-execucao-ix-px-cx-ux-scrubbing-ambiente.
- [[selinux-arquitetura-mac-baseada-rotulos-type-enforcement-contextos]] — Referência cruzada direta com selinux-arquitetura-mac-baseada-rotulos-type-enforcement-contextos.

## Fontes
- [AppArmor Official GitLab — Kernel LSM & Userspace Architecture](https://gitlab.com/apparmor/apparmor/-/raw/master/README.md) — documentação oficial do projeto AppArmor cobrindo o módulo LSM do kernel, libapparmor, parser e utilitários; consultado em 2026-10-03.
- [AppArmor Official Wiki — Home & Profiles Overview](https://gitlab.com/apparmor/apparmor/-/wikis/home) — wiki oficial do AppArmor sobre perfis de confinamento, distribuições e ferramentas de política; consultado em 2026-10-03.
- [AppArmor Official Wiki — Technical Documentation](https://gitlab.com/apparmor/apparmor/-/wikis/Documentation) — documentação técnica da linguagem de perfis, transições de execução e abstrações do AppArmor; consultado em 2026-10-03.
