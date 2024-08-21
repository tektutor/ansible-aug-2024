from ansible.module_utils.basic import AnsibleModule

def sayHello(greeting):
    return "Hello " + greeting + "!"

def main():
    module = AnsibleModule(
        argument_spec=dict(
            message=dict(type='str'),
        ),
        supports_check_mode=True
    )

    result = dict(
        response=sayHello(module.params['message']),
    )

    module.exit_json(**result)


if __name__ == '__main__':
    main()
