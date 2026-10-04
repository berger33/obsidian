---
id: software.seguranca.tranche14.001400
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
fontes: ["https://raw.githubusercontent.com/tpm2-software/tpm2-tools/master/README.md", "https://raw.githubusercontent.com/tpm2-software/tpm2-tss/master/README.md"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# Testes Automatizados em CI/CD e Virtualização (**`vTPM`**) com **`swtpm` (`libtpms`)** e Seleção de **`TCTI` (`TPM2TOOLS_TCTI`)** no `tpm2-tss`

## Em uma frase
Como testar scripts de provisionamento, selagem de segredos (`tpm2_create`, `tpm2_unseal`), atestação remota (`tpm2_quote`) e integração PKCS#11 dentro de um **pipeline de CI/CD (GitHub Actions / GitLab CI) ou container Docker** que não possui um chip TPM 2.0 físico dedicado, e como fornecer um **vTPM 2.0** isolado para máquinas virtuais **QEMU/KVM (`libvirt`)**?

## Por que importa
Graças à arquitetura modular da camada **`TCTI` (*TPM Command Transmission Interface*)** da `tpm2-tss` combinada com o emulador oficial de TPM 2.0 **`swtpm` (baseado na biblioteca `libtpms`)**!

## Como funciona
Em vez de falar com o dispositivo de hardware `/dev/tpmrm0`, basta iniciar um processo **`swtpm socket`** em espaço de usuário (sem precisar de `root` nem de hardware físico!) e exportar a variável de ambiente **`TPM2TOOLS_TCTI="swtpm:host=127.0.0.1,port=2321"`** (ou passar `-T swtpm:...` para qualquer comando `tpm2_*`): todos os comandos do `tpm2-tools`, da `libtss2-esys` e do `tpm2-pkcs11` funcionam de forma **100% idêntica a um chip físico**!

## Exemplo
```bash
# Iniciar um emulador de TPM 2.0 em software (swtpm) em um diretorio temporario, inicializar o chip (tpm2_startup) e rodar testes via TCTI swtpm
mkdir -p /tmp/meu-vtpm-ci
swtpm socket --tpm2 --tpmstate dir=/tmp/meu-vtpm-ci \
  --ctrl type=tcp,port=2322 --server type=tcp,port=2321 \
  --flags not-need-init,startup-clear --daemon
export TPM2TOOLS_TCTI="swtpm:host=127.0.0.1,port=2321"
tpm2_getcap properties-fixed | head -n 15
tpm2_getrandom --hex 16
```

## Limites e trade-offs
Olhe que facilidade para escrever testes de integração de segurança no seu CI/CD com as 6 linhas acima: você sobe um TPM 2.0 limpo em `/tmp/meu-vtpm-ci` em menos de 50 milissegundos, testa toda a sua lógica de `tpm2_createprimary`, `tpm2_createpolicy`, `tpm2_quote` e `tpm2_unseal`, e apaga a pasta ao final do teste!

## Como verificar
E em hipervisores **QEMU/KVM (`libvirt` / Proxmox / OpenStack)**, o mesmo **`swtpm`** é integrado nativamente para fornecer um **`vTPM 2.0` exclusivo para cada máquina virtual** (com o estado NVRAM do `swtpm` cifrado no host hipervisor!), permitindo que VMs Linux e Windows usem **Measured Boot, LUKS2 (`systemd-cryptenroll`) e BitLocker** exatamente como em servidores bare-metal!

## Conexões
- [[tpm2-protecao-forca-bruta-dictionary-attack-lockout-clear-seguranca]] — Veja também: Proteção Contra Força Bruta em Hardware (**Dictionary Attack Lockout**: `tpm2_dictionarylockout`), Senhas de Hierarquia (`tpm2_changeauth`) e **TRNG (`tpm2_getrandom`)**.
- [[tpm2-arquitetura-trusted-platform-module-tss-hierarquias-pcrs]] — Referência cruzada direta com tpm2-arquitetura-trusted-platform-module-tss-hierarquias-pcrs.
- [[tpm2-atestacao-remota-ak-ek-tpm2-quote-checkquote-verificacao]] — Referência cruzada direta com tpm2-atestacao-remota-ak-ek-tpm2-quote-checkquote-verificacao.
- [[tpm2-selagem-segredos-sealing-unsealing-pcr-policy-luks-systemd-cryptenroll]] — Referência cruzada direta com tpm2-selagem-segredos-sealing-unsealing-pcr-policy-luks-systemd-cryptenroll.

## Fontes
- [Official `tpm2-tools` GitHub Repository (`tpm2-software/tpm2-tools`)](https://raw.githubusercontent.com/tpm2-software/tpm2-tools/master/README.md) — repositório oficial dos utilitários `tpm2-tools` cobrindo criação de chaves, selagem em PCRs, políticas EA, cotações de atestação remota (`tpm2_quote`), NVRAM e Dictionary Attack Lockout; consultado em 2026-10-03.
- [Official TCG TPM2 Software Stack (`tpm2-software/tpm2-tss`) GitHub Repository](https://raw.githubusercontent.com/tpm2-software/tpm2-tss/master/README.md) — documentação oficial da pilha `tpm2-tss` detalhando as camadas arquiteturais `libtss2-fapi`, `libtss2-esys`, `libtss2-sys`, `libtss2-mu` e módulos `TCTI` (`device`, `swtpm`, `mssim`, `tctildr`); consultado em 2026-10-03.
